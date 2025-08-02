# Claude Brain Installation Guide

This guide covers the complete installation of Claude Brain, including all components needed for full functionality.

## Prerequisites

- macOS (tested on macOS 15.6)
- Node.js 18+ (for MCP server)
- Python 3.9+ (for execution server)
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- Claude Desktop app

## Step 1: Clone the Repository

```bash
cd ~/Code
git clone https://github.com/yourusername/claude-brain.git
cd claude-brain
```

## Step 2: Install Main Dependencies

```bash
# Install Node.js dependencies for MCP server
npm install

# Install Python dependencies for monitoring (optional)
uv pip install -e ".[monitor]"
```

## Step 3: Set Up Execution Server

The execution server is required for the `brain_execute` function to work.

### 3.1 Create Execution Server Directory

```bash
# Create directory
mkdir -p ~/Code/mcp-execution-server
cd ~/Code/mcp-execution-server

# Copy server file (from claude-brain repo or create new)
# The server.py file handles code execution requests
```

### 3.2 Initialize Python Environment

```bash
cd ~/Code/mcp-execution-server

# Create pyproject.toml
cat > pyproject.toml << 'EOF'
[project]
name = "mcp-execution-server"
version = "1.0.0"
description = "Brain MCP Execution Server"
requires-python = ">=3.9"

[tool.uv]
dev-dependencies = []
EOF

# Initialize virtual environment
uv venv
```

### 3.3 Install as System Service (Recommended)

Create the LaunchAgent configuration:

```bash
# Create the plist file
cat > ~/Library/LaunchAgents/com.user.brain-execution-server.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.brain-execution-server</string>
    
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/uv</string>
        <string>run</string>
        <string>python</string>
        <string>/home/edgar/github/mcp-execution-server/server.py</string>
    </array>
    
    <key>WorkingDirectory</key>
    <string>/home/edgar/github/mcp-execution-server</string>
    
    <key>RunAtLoad</key>
    <true/>
    
    <key>KeepAlive</key>
    <dict>
        <key>SuccessfulExit</key>
        <false/>
        <key>Crashed</key>
        <true/>
    </dict>
    
    <key>StandardOutPath</key>
    <string>/home/edgar/Library/Logs/brain-execution-server.log</string>
    
    <key>StandardErrorPath</key>
    <string>/home/edgar/Library/Logs/brain-execution-server.error.log</string>
    
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin</string>
        <key>HOME</key>
        <string>/home/edgar</string>
    </dict>
    
    <key>ThrottleInterval</key>
    <integer>10</integer>
</dict>
</plist>
EOF

# Load and start the service
launchctl load ~/Library/LaunchAgents/com.user.brain-execution-server.plist
launchctl start com.user.brain-execution-server

# Verify it's running
curl http://localhost:9998/
```

## Step 4: Configure Claude Desktop

Add the Brain MCP server to your Claude Desktop configuration:

1. Open Claude Desktop settings
2. Navigate to Developer > Edit Config
3. Add the following to your config:

```json
{
  "mcpServers": {
    "claude-brain": {
      "command": "node",
      "args": ["/home/edgar/github/claude-brain/index.js"]
    }
  }
}
```

4. Restart Claude Desktop

## Step 5: Configure Claude's System Prompt

To enable automatic brain initialization, add this to your Claude Desktop user preferences:

```
At the start of each session, use brain_init to load my preferences and context. 
Projects are usually in the Code directory. 
For a complete directory of stored knowledge, use brain_recall "index". 
To see the last project worked on, use brain_recall "last_project". 
The Brain contains all persistent context and instructions for development work.
```

## Step 6: Verify Installation

1. **Check Execution Server**:
   ```bash
   # Should return server info
   curl http://localhost:9998/
   
   # Check service status
   launchctl list | grep brain-execution
   ```

2. **Test in Claude Desktop**:
   - Start a new conversation
   - Ask Claude to "initialize brain session" or wait for auto-init
   - Try: "Can you execute `print('Hello from Brain!')`"

## Optional: Monitoring UI

To enable real-time monitoring of executions:

```bash
cd ~/Code/claude-brain/monitor
python server.py
```

Then open: http://localhost:9996

## Troubleshooting

### Execution Server Issues

1. **Port already in use**:
   ```bash
   # Find and kill process on port 9998
   lsof -ti:9998 | xargs kill -9
   ```

2. **Service won't start**:
   ```bash
   # Check logs
   tail -f ~/Library/Logs/brain-execution-server.error.log
   
   # Try manual start
   cd ~/Code/mcp-execution-server
   uv run python server.py
   ```

3. **Permission issues**:
   - Ensure uv is in PATH: `/usr/local/bin/uv`
   - Check file permissions on server.py

### MCP Server Issues

1. **Tools not available in Claude**:
   - Verify absolute path in Claude config
   - Restart Claude Desktop
   - Check Claude Desktop logs

2. **Database errors**:
   - Check permissions on `~/Code/claude-brain/data/`
   - Delete brain.db to start fresh (loses memory)

## Uninstallation

To completely remove Claude Brain:

```bash
# Stop and remove execution server
launchctl stop com.user.brain-execution-server
launchctl unload ~/Library/LaunchAgents/com.user.brain-execution-server.plist
rm ~/Library/LaunchAgents/com.user.brain-execution-server.plist

# Remove from Claude config
# Edit Claude Desktop config and remove the claude-brain entry

# Remove files (optional - this deletes all memories!)
rm -rf ~/Code/claude-brain
rm -rf ~/Code/mcp-execution-server
```

## Security Notes

- The execution server runs with your user permissions
- All executions are logged to `~/Library/Logs/brain-execution-server.log`
- Monitor executions via the web UI or logs
- Only install on systems where you trust Claude with code execution

## Next Steps

- Read the [Architecture Documentation](ARCHITECTURE.md)
- Check the [API Reference](API.md)
- Join the community discussions
