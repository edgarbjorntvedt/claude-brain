#!/usr/bin/env python3
"""
Brain Execution Log API Server - Fixed Version
"""

import json
import os
import glob
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

LOG_DIR = "/Users/bard/Code/claude-brain/data/logs/execution"
PORT = 9998

class LogAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        # Enable CORS
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        if parsed_path.path == '/':
            # Root endpoint
            self.wfile.write(json.dumps({
                "service": "Brain Execution API",
                "version": "1.0.3",
                "endpoints": [
                    "/health - API health check",
                    "/api/brain/executions - List recent executions",
                    "/api/brain/executions/{id} - Get specific execution log",
                ],
                "log_dir": LOG_DIR
            }).encode())
            
        elif parsed_path.path == '/api/brain/executions':
            self.handle_list_executions()
            
        elif parsed_path.path.startswith('/api/brain/executions/'):
            execution_id = parsed_path.path.split('/')[-1]
            self.handle_get_execution(execution_id)
            
        elif parsed_path.path == '/health':
            self.wfile.write(json.dumps({
                "status": "healthy",
                "service": "brain-execution-api",
                "version": "1.0.3"
            }).encode())
            
        else:
            self.wfile.write(json.dumps({"error": "Unknown endpoint"}).encode())
    
    def handle_list_executions(self):
        """List recent execution logs"""
        try:
            os.makedirs(LOG_DIR, exist_ok=True)
            
            # Find all execution logs
            log_files = glob.glob(os.path.join(LOG_DIR, "exec-*.json"))
            executions = []
            
            # Sort by modification time, newest first
            log_files.sort(key=os.path.getmtime, reverse=True)
            
            for log_file in log_files[:50]:  # Limit to 50 most recent
                try:
                    with open(log_file, 'r') as f:
                        data = json.load(f)
                    
                    # Create execution summary
                    execution = {
                        "id": data.get('execution_id', data.get('id', os.path.basename(log_file))),
                        "timestamp": data.get('timestamp', ''),
                        "language": data.get('language', data.get('type', 'unknown')),
                        "status": data.get('status', 'completed'),
                        "description": data.get('description', ''),
                        "file": os.path.basename(log_file)
                    }
                    executions.append(execution)
                    
                except Exception as e:
                    print(f"Error reading {log_file}: {e}")
                    continue
            
            self.wfile.write(json.dumps({
                "executions": executions,
                "count": len(executions)
            }).encode())
            
        except Exception as e:
            self.wfile.write(json.dumps({
                "error": str(e),
                "executions": [],
                "count": 0
            }).encode())
    
    def handle_get_execution(self, execution_id):
        """Get specific execution log details"""
        try:
            # Try to find the file
            possible_files = [
                os.path.join(LOG_DIR, f"{execution_id}.json"),
                os.path.join(LOG_DIR, f"exec-{execution_id}.json"),
            ]
            
            # Also search by ID in files
            for file in glob.glob(os.path.join(LOG_DIR, "exec-*.json")):
                try:
                    with open(file, 'r') as f:
                        data = json.load(f)
                    if data.get('id') == execution_id or data.get('execution_id') == execution_id:
                        self.wfile.write(json.dumps(data).encode())
                        return
                except:
                    continue
            
            # Try direct file paths
            for file_path in possible_files:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    self.wfile.write(json.dumps(data).encode())
                    return
            
            self.wfile.write(json.dumps({"error": "Execution not found"}).encode())
            
        except Exception as e:
            self.wfile.write(json.dumps({"error": str(e)}).encode())

def run_server():
    """Run the API server"""
    server = HTTPServer(('localhost', PORT), LogAPIHandler)
    print(f"Brain Execution API running on port {PORT}")
    print(f"Log directory: {LOG_DIR}")
    server.serve_forever()

if __name__ == '__main__':
    run_server()
