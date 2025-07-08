"""
Brain Analyzer for Obsidian Vault
"""
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict, Counter
import re
import datetime


class BrainAnalyzer:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
    
    def _parse_frontmatter(self, content: str) -> tuple[Dict[str, Any], str]:
        """Parse frontmatter from markdown content."""
        if content.startswith('---\\n'):
            try:
                end_index = content.index('\\n---\\n', 4)
                frontmatter_text = content[4:end_index]
                body = content[end_index + 5:]
                
                frontmatter = {}
                for line in frontmatter_text.strip().split('\\n'):
                    if ': ' in line:
                        key, value = line.split(': ', 1)
                        try:
                            value = json.loads(value)
                        except:
                            pass
                        frontmatter[key.strip()] = value
                
                return frontmatter, body
            except ValueError:
                pass
        
        return {}, content
    
    def _extract_links(self, content: str) -> List[str]:
        """Extract wiki-style links from content."""
        # Match [[Link]] and [[Link|Display]]
        pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
        matches = re.findall(pattern, content)
        return matches
    
    def analyze_connections(self) -> Dict[str, Any]:
        """Analyze connections between notes."""
        connections = defaultdict(list)
        backlinks = defaultdict(list)
        
        for note_path in self.vault_path.rglob('*.md'):
            note_name = note_path.stem
            content = note_path.read_text(encoding='utf-8')
            _, body = self._parse_frontmatter(content)
            
            links = self._extract_links(body)
            connections[note_name] = links
            
            for link in links:
                backlinks[link].append(note_name)
        
        return {
            'connections': dict(connections),
            'backlinks': dict(backlinks),
            'total_notes': len(connections),
            'total_links': sum(len(links) for links in connections.values())
        }
    
    def find_orphans(self) -> Dict[str, Any]:
        """Find notes with no incoming or outgoing links."""
        analysis = self.analyze_connections()
        all_notes = set()
        linked_notes = set()
        
        for note_path in self.vault_path.rglob('*.md'):
            all_notes.add(note_path.stem)
        
        # Notes that have outgoing links
        for note, links in analysis['connections'].items():
            if links:
                linked_notes.add(note)
        
        # Notes that have incoming links
        for note, backlinks in analysis['backlinks'].items():
            if backlinks:
                linked_notes.add(note)
        
        orphans = list(all_notes - linked_notes)
        
        return {
            'orphans': orphans,
            'count': len(orphans),
            'percentage': (len(orphans) / len(all_notes) * 100) if all_notes else 0
        }
    
    def analyze_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in the vault."""
        tag_counter = Counter()
        word_counter = Counter()
        note_count = 0
        total_words = 0
        
        for note_path in self.vault_path.rglob('*.md'):
            note_count += 1
            content = note_path.read_text(encoding='utf-8')
            metadata, body = self._parse_frontmatter(content)
            
            # Count tags
            if 'tags' in metadata:
                tags = metadata['tags']
                if isinstance(tags, list):
                    tag_counter.update(tags)
                elif isinstance(tags, str):
                    tag_counter[tags] += 1
            
            # Count words (simple approach)
            words = re.findall(r'\\b\\w+\\b', body.lower())
            total_words += len(words)
            # Only count meaningful words (length > 3)
            meaningful_words = [w for w in words if len(w) > 3]
            word_counter.update(meaningful_words)
        
        return {
            'note_count': note_count,
            'total_words': total_words,
            'average_words_per_note': total_words / note_count if note_count else 0,
            'top_tags': tag_counter.most_common(10),
            'top_words': word_counter.most_common(20)
        }
    
    def generate_insights(self) -> Dict[str, Any]:
        """Generate insights about the vault."""
        insights = []
        
        # Get basic stats
        patterns = self.analyze_patterns()
        orphans = self.find_orphans()
        connections = self.analyze_connections()
        
        # Generate insights
        if patterns['note_count'] == 0:
            insights.append({
                'type': 'warning',
                'message': 'Your vault is empty. Start creating notes!'
            })
        else:
            insights.append({
                'type': 'info',
                'message': f"Your vault contains {patterns['note_count']} notes with {patterns['total_words']} total words"
            })
        
        if orphans['percentage'] > 50:
            insights.append({
                'type': 'suggestion',
                'message': f"{orphans['percentage']:.1f}% of your notes are orphaned. Consider linking them to other notes."
            })
        
        if patterns['top_tags']:
            most_used_tag = patterns['top_tags'][0]
            insights.append({
                'type': 'info',
                'message': f"Your most used tag is '{most_used_tag[0]}' with {most_used_tag[1]} occurrences"
            })
        
        avg_connections = connections['total_links'] / patterns['note_count'] if patterns['note_count'] else 0
        if avg_connections < 1:
            insights.append({
                'type': 'suggestion',
                'message': 'Your notes have few connections. Try linking related concepts together.'
            })
        
        return {
            'insights': insights,
            'generated_at': datetime.datetime.now().isoformat()
        }
    
    def full_analysis(self, save_report: bool = False) -> Dict[str, Any]:
        """Perform full analysis of the vault."""
        analysis = {
            'patterns': self.analyze_patterns(),
            'connections': self.analyze_connections(),
            'orphans': self.find_orphans(),
            'insights': self.generate_insights()
        }
        
        if save_report:
            report_path = self.vault_path / '_analysis_report.md'
            report_content = f"""---
generated_at: {datetime.datetime.now().isoformat()}
type: analysis_report
---

# Vault Analysis Report

Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview
- Total Notes: {analysis['patterns']['note_count']}
- Total Words: {analysis['patterns']['total_words']}
- Average Words per Note: {analysis['patterns']['average_words_per_note']:.0f}

## Connections
- Total Links: {analysis['connections']['total_links']}
- Orphaned Notes: {analysis['orphans']['count']} ({analysis['orphans']['percentage']:.1f}%)

## Top Tags
{chr(10).join(f"- {tag}: {count}" for tag, count in analysis['patterns']['top_tags'][:5])}

## Insights
{chr(10).join(f"- **{insight['type']}**: {insight['message']}" for insight in analysis['insights']['insights'])}

## Top Words
{', '.join(word for word, _ in analysis['patterns']['top_words'][:10])}
"""
            report_path.write_text(report_content, encoding='utf-8')
            analysis['report_saved'] = str(report_path)
        
        return analysis
