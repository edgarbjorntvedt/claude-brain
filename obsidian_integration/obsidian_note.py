"""
Obsidian Note Integration for Brain MCP Server
"""
import os
import json
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Import Mercury tracker
try:
    from .mercury_tracker import mercury_tracker
except ImportError:
    # Create a dummy tracker if import fails
    class DummyTracker:
        def track_note_access(self, *args, **kwargs):
            pass
    mercury_tracker = DummyTracker()


class ObsidianNote:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        if not self.vault_path.exists():
            self.vault_path.mkdir(parents=True, exist_ok=True)
    
    def _ensure_folder(self, folder_path: Path) -> None:
        """Ensure a folder exists in the vault."""
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
    
    def _get_note_path(self, identifier: str) -> Path:
        """Get the full path for a note."""
        # Remove .md extension if provided
        if identifier.endswith('.md'):
            identifier = identifier[:-3]
        return self.vault_path / f"{identifier}.md"
    
    def _parse_frontmatter(self, content: str) -> tuple[Dict[str, Any], str]:
        """Parse frontmatter from markdown content."""
        if content.startswith('---\n'):
            try:
                end_index = content.index('\n---\n', 4)
                frontmatter_text = content[4:end_index]
                body = content[end_index + 5:]
                
                # Simple YAML parsing (basic implementation)
                frontmatter = {}
                for line in frontmatter_text.strip().split('\n'):
                    if ': ' in line:
                        key, value = line.split(': ', 1)
                        # Try to parse JSON values
                        try:
                            value = json.loads(value)
                        except:
                            # Keep as string if not JSON
                            pass
                        frontmatter[key.strip()] = value
                
                return frontmatter, body
            except ValueError:
                # No closing frontmatter
                pass
        
        return {}, content
    
    def _create_frontmatter(self, metadata: Dict[str, Any]) -> str:
        """Create frontmatter from metadata."""
        if not metadata:
            return ""
        
        lines = ["---"]
        for key, value in metadata.items():
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            lines.append(f"{key}: {value}")
        lines.append("---")
        return '\n'.join(lines) + '\n\n'
    
    def create(self, title: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a new note in the vault."""
        try:
            note_path = self._get_note_path(title)
            
            # Check if note already exists
            if note_path.exists():
                return {"error": f"Note '{title}' already exists"}
            
            # Ensure parent directory exists
            self._ensure_folder(note_path.parent)
            
            # Add default metadata
            if metadata is None:
                metadata = {}
            metadata['created'] = datetime.datetime.now().isoformat()
            metadata['modified'] = metadata['created']
            
            # Create content with frontmatter
            full_content = self._create_frontmatter(metadata) + content
            
            # Write the file
            note_path.write_text(full_content, encoding='utf-8')
            
            # Track in Mercury Evolution
            mercury_tracker.track_note_access('create', title)
            
            return {
                "success": True,
                "identifier": title,
                "path": str(note_path.relative_to(self.vault_path)),
                "metadata": metadata
            }
        except Exception as e:
            return {"error": str(e)}
    
    def read(self, identifier: str) -> Dict[str, Any]:
        """Read a note from the vault."""
        try:
            note_path = self._get_note_path(identifier)
            
            if not note_path.exists():
                return {"error": f"Note '{identifier}' not found"}
            
            content = note_path.read_text(encoding='utf-8')
            metadata, body = self._parse_frontmatter(content)
            
            # Track in Mercury Evolution
            mercury_tracker.track_note_access('read', identifier)
            
            return {
                "success": True,
                "identifier": identifier,
                "content": body,
                "metadata": metadata,
                "path": str(note_path.relative_to(self.vault_path))
            }
        except Exception as e:
            return {"error": str(e)}
    
    def update(self, identifier: str, content: Optional[str] = None, metadata_updates: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Update an existing note."""
        try:
            note_path = self._get_note_path(identifier)
            
            if not note_path.exists():
                return {"error": f"Note '{identifier}' not found"}
            
            # Read existing content
            existing_content = note_path.read_text(encoding='utf-8')
            existing_metadata, existing_body = self._parse_frontmatter(existing_content)
            
            # Update metadata
            if metadata_updates:
                existing_metadata.update(metadata_updates)
            existing_metadata['modified'] = datetime.datetime.now().isoformat()
            
            # Use new content if provided, otherwise keep existing
            body = content if content is not None else existing_body
            
            # Create updated content
            full_content = self._create_frontmatter(existing_metadata) + body
            
            # Write the file
            note_path.write_text(full_content, encoding='utf-8')
            
            # Track in Mercury Evolution
            mercury_tracker.track_note_access('update', identifier)
            
            return {
                "success": True,
                "identifier": identifier,
                "path": str(note_path.relative_to(self.vault_path)),
                "metadata": existing_metadata
            }
        except Exception as e:
            return {"error": str(e)}
    
    def delete(self, identifier: str) -> Dict[str, Any]:
        """Delete a note from the vault."""
        try:
            note_path = self._get_note_path(identifier)
            
            if not note_path.exists():
                return {"error": f"Note '{identifier}' not found"}
            
            # Delete the file
            note_path.unlink()
            
            # Track in Mercury Evolution
            mercury_tracker.track_note_access('delete', identifier)
            
            return {
                "success": True,
                "identifier": identifier,
                "message": f"Note '{identifier}' deleted successfully"
            }
        except Exception as e:
            return {"error": str(e)}
    
    def list_notes(self, folder: Optional[str] = None) -> Dict[str, Any]:
        """List all notes in the vault or a specific folder."""
        try:
            search_path = self.vault_path
            if folder and folder != '.':
                search_path = self.vault_path / folder
            
            if not search_path.exists():
                return {"error": f"Folder '{folder}' not found"}
            
            notes = []
            for note_path in search_path.rglob('*.md'):
                # Skip files outside vault (e.g., symlinks)
                try:
                    relative_path = note_path.relative_to(self.vault_path)
                except ValueError:
                    continue
                identifier = str(relative_path)[:-3]  # Remove .md extension
                
                # Try to get metadata
                try:
                    content = note_path.read_text(encoding='utf-8')
                    metadata, _ = self._parse_frontmatter(content)
                except:
                    metadata = {}
                
                notes.append({
                    "identifier": identifier,
                    "path": str(relative_path),
                    "metadata": metadata
                })
            
            # Track in Mercury Evolution if we have results
            if notes:
                mercury_tracker.track_note_access('list', folder or 'vault')
            
            return {
                "success": True,
                "count": len(notes),
                "notes": notes
            }
        except Exception as e:
            return {"error": str(e)}
