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
            
            # Search in memories table using FTS5 if available
            try:
                # Try FTS5 first for better search
                cursor.execute("""
                    SELECT key, value, type, created_at
                    FROM memories
                    WHERE rowid IN (
                        SELECT rowid FROM memories_fts
                        WHERE memories_fts MATCH ?
                    )
                    ORDER BY created_at DESC
                    LIMIT ?
                """, (query, limit))
            except:
                # Fallback to LIKE search
                cursor.execute("""
                    SELECT key, value, type, created_at
                    FROM memories
                    WHERE key LIKE ? OR value LIKE ?
                    ORDER BY created_at DESC
                    LIMIT ?
                """, (f'%{query}%', f'%{query}%', limit))
            
            results = []
            for row in cursor.fetchall():
                # Truncate value to prevent JSON parsing issues
                value = row['value']
                if len(value) > 150:
                    value = value[:150] + '...'

                results.append({
                    'source': 'brain',
                    'type': row['type'],
                    'key': row['key'],
                    'value': value,
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
        brain_results = []
        obsidian_results = []

        if source in ['all', 'brain']:
            brain_results = self.search_brain(query, limit)

        if source in ['all', 'obsidian']:
            obsidian_results = self.search_obsidian(query, limit)

        # Merge and limit results
        all_results = brain_results + obsidian_results
        merged = all_results[:limit]

        return {
            'query': query,
            'brain_count': len(brain_results),
            'obsidian_count': len(obsidian_results),
            'merged': merged,
            'count': len(merged)
        }


if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 4:
        print("Usage: python unified_search.py <query> <limit> <source>")
        sys.exit(1)

    query = sys.argv[1]
    limit = int(sys.argv[2])
    source = sys.argv[3]

    # Get paths from config
    brain_db_path = os.path.expanduser("~/.claude-brain/brain/brain/brain.db")
    vault_path = os.path.expanduser("~/.claude-brain/brain/BrainVault")

    searcher = UnifiedSearch(brain_db_path, vault_path)
    results = searcher.search(query, limit, source)

    print(json.dumps(results, indent=2))
