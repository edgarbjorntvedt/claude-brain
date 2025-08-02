"""
Mercury Evolution integration for Brain
Tracks note access patterns
"""
import subprocess
import json
import os
from typing import Optional

class MercuryTracker:
    """Tracks note access in Mercury Evolution"""
    
    def __init__(self):
        self.mercury_cli = "/home/edgar/github/mcp-mercury-evolution/dist/mercury-track.js"
        self.enabled = os.path.exists(self.mercury_cli)
        
    def track_note_access(self, action: str, path: str, from_note: Optional[str] = None):
        """Track a note access in Mercury Evolution"""
        if not self.enabled:
            return False
            
        try:
            # Call Mercury CLI tool
            cmd = ['node', self.mercury_cli, action, path]
            if from_note:
                cmd.extend(['--from', from_note])
                
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=1  # Don't block Brain
            )
            
            if result.returncode == 0:
                return True
            else:
                # Log error but don't fail
                if result.stderr:
                    print(f"Mercury tracking error: {result.stderr}")
                return False
                
        except Exception as e:
            # Silently fail - tracking is optional
            return False

# Global instance
mercury_tracker = MercuryTracker()
