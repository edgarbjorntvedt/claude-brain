# Claude Brain Installation Guide

**📍 Path Assumptions**: This guide assumes you have cloned the project to `~/Code/claude-brain`. If you're using a 
different location, adjust the paths accordingly throughout this document.


This guide covers the complete installation of Claude Brain, including all components needed for full functionality.

## Prerequisites

- macOS (tested on macOS 15.6)
- Node.js 18+ (for MCP server)
- Python 3.9+ (for integrated code execution)
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

## Step 3: Configure Claude Desktop

Add the Brain MCP server to your Claude Desktop configuration:

1. Open Claude Desktop settings
2. Navigate to Developer > Edit Config
3. Add the following to your config:

```json
{
  "mcpServers": {
    "claude-brain": {
      "command": "node",
      "args": ["~/Code/claude-brain/index.js"]
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

1. **Test in Claude Desktop**:
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

### MCP Server Issues

1. **Tools not available in Claude**:
   - Verify absolute path in Claude config
   - Restart Claude Desktop
   - Check Claude Desktop logs

2. **Database errors**:
   - Check permissions on `~/Code/claude-brain/data/`
   - Delete brain.db to start fresh (loses memory)

3. **Permission issues**:
   - Ensure uv is in PATH: `/usr/local/bin/uv`
   - Check file permissions on server.py

## Uninstallation

To completely remove Claude Brain:

```bash
# Remove from Claude config
# Edit Claude Desktop config and remove the claude-brain entry

# Remove files (optional - this deletes all memories!)
rm -rf ~/Code/claude-brain
```

## Security Notes

- Code execution runs with your user permissions via Node.js child processes
- All executions are logged within the MCP server process
- Monitor executions via the web UI or logs
- Only install on systems where you trust Claude with code execution

## Next Steps

- Read the [Architecture Documentation](ARCHITECTURE.md)
- Check the [API Reference](API.md)
- Join the community discussions
