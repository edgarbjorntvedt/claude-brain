"""
Unified Search for Brain and Obsidian
"""
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import sqlite3


class UnifiedSearch:
    def __init__(self, brain_db_path: str, vault_path: str):
        self.brain_db_path = brain_db_path
        self.vault_path = Path(vault_path)
    
    def search_brain(self, query: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Search brain memories."""
        try:
            conn = sqlite3.connect(self.brain_db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Search in brain_memories table
            cursor.execute("""
                SELECT key, value, type, created_at
                FROM memories
                WHERE key LIKE ? OR value LIKE ?
                ORDER BY created_at DESC
                LIMIT ?
            """, (f'%{query}%', f'%{query}%', limit))
            
            results = []
            for row in cursor.fetchall():
                results.append({
                    'source': 'brain',
                    'type': row['type'],
                    'key': row['key'],
                    'value': row['value'][:200] + '...' if len(row['value']) > 200 else row['value'],
                    'created_at': row['created_at']
                })
            
            conn.close()
            return results
        except Exception as e:
            return [{'source': 'brain', 'error': str(e)}]
    
    def search_obsidian(self, query: str, limit: int = 20) -> List[Dict[str, Any]]:
        """Search Obsidian notes."""
        try:
            results = []
            query_lower = query.lower()
            
            for note_path in self.vault_path.rglob('*.md'):
                if len(results) >= limit:
                    break
                
                try:
                    content = note_path.read_text(encoding='utf-8')
                    title = note_path.stem
                    
                    # Check if query matches title or content
                    if query_lower in title.lower() or query_lower in content.lower():
                        # Extract first 200 chars of content (skip frontmatter)
                        preview = content
                        if preview.startswith('---\\n'):
                            try:
                                end_idx = preview.index('\\n---\\n', 4) + 5
                                preview = preview[end_idx:]
                            except:
                                pass
                        
                        preview = preview.strip()[:200] + '...' if len(preview) > 200 else preview.strip()
                        
                        results.append({
                            'source': 'obsidian',
                            'type': 'note',
                            'title': title,
                            'path': str(note_path.relative_to(self.vault_path)),
                            'preview': preview
                        })
                except Exception:
                    continue
            
            return results
        except Exception as e:
            return [{'source': 'obsidian', 'error': str(e)}]
    
    def search(self, query: str, limit: int = 20, source: str = 'all') -> Dict[str, Any]:
        """Unified search across brain and obsidian."""
        results = {
            'query': query,
            'results': []
        }
        
        if source in ['all', 'brain']:
            brain_results = self.search_brain(query, limit)
            results['results'].extend(brain_results)
        
        if source in ['all', 'obsidian']:
            obsidian_results = self.search_obsidian(query, limit)
            results['results'].extend(obsidian_results)
        
        # Limit total results
        results['results'] = results['results'][:limit]
        results['count'] = len(results['results'])
        
        return results
