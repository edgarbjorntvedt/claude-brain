# Claude Brain 🧠

A unified, clean, and simple persistent memory system for Claude via MCP (Model Context Protocol).

## Overview

Claude Brain provides Claude with persistent memory across conversations, combining the best features from previous implementations into a single, maintainable codebase.

**Important**: This project is specifically designed for the Claude Desktop app, bringing API-level capabilities like memory persistence and code execution to app users who previously had no access to these features.

## Features

- 🧠 **Persistent Memory**: Store and recall information across sessions
- 📊 **Execution Monitoring**: Track and visualize Claude's code execution
- 🔍 **Unified Search**: Search across memories and notes
- 🚀 **Simple Setup**: One-command installation
- 🎯 **Clean Architecture**: Minimal dependencies, maximum functionality

## Quick Start

1. **Install dependencies**:
   ```bash
   # Install Node.js dependencies
   npm install
   
   # Install Python monitoring tools (optional)
   uv pip install -e ".[monitor]"
   ```

2. **Set up the Execution Server** (Required for `brain_execute`):
   The execution server runs on port 9998 and handles code execution requests.
   
   ```bash
   # Navigate to execution server directory
   cd ~/Code/mcp-execution-server
   
   # Initialize with uv
   uv venv
   
   # Install as a service (auto-starts on login)
   cp ~/Desktop/com.user.brain-execution-server.plist ~/Library/LaunchAgents/
   launchctl load ~/Library/LaunchAgents/com.user.brain-execution-server.plist
   launchctl start com.user.brain-execution-server
   
   # Verify it's running
   curl http://localhost:9998/
   ```
   
   **Note**: The execution server must be running for `brain_execute` to work.

3. **Configure Claude Desktop**:
   Add to your Claude Desktop config:
   ```json
   {
     "mcpServers": {
       "claude-brain": {
         "command": "node",
         "args": ["/path/to/claude-brain/index.js"]
       }
     }
   }
   ```

4. **Configure Claude's System Message (IMPORTANT)**:
   To get Claude to automatically use the brain tools, add this to your Claude Desktop user preferences:
   
   ```
   At the start of each session, use brain_init to load my preferences and context. 
   For a complete directory of stored knowledge, use brain_recall "index". 
   To see the last project worked on, use brain_recall "last_project".
   ```
   
   Or for more comprehensive initialization:
   ```
   At the start of each session, use brain_init to load my preferences and context. 
   Projects are usually in the Code directory. 
   For a complete directory of stored knowledge, use brain_recall "index". 
   To see the last project worked on, use brain_recall "last_project". 
   The Brain contains all persistent context and instructions for development work. 
   Start with brain_init to load core context. 
   For detailed guidance: brain_recall 'user manual' or 'init loading strategy'.
   ```

5. **Available Brain Functions**:
   - `brain_init` - Initialize your session and load context
   - `brain_remember(key, value, type)` - Store information
   - `brain_recall(query)` - Search and retrieve memories
   - `brain_execute(code, language)` - Execute Python or shell commands
   - `brain_status()` - Check system status
   - `brain_analyze()` - Analyze vault for insights and connections
   
   **State Management Functions**:
   - `state_set(key, value, category)` - Set state values
   - `state_get(key)` - Retrieve state values
   - `state_list(category)` - List state entries
   - `state_delete(key)` - Delete state entries
   
   **Obsidian Integration**:
   - `obsidian_note(action, ...)` - Create/read/update/delete notes
   - `unified_search(query)` - Search across brain and Obsidian

## Usage Examples

### Basic Memory Operations
```
# Initialize at the start of a conversation
Me: Hi Claude, please initialize our session
Claude: [executes brain_init()]

# Store project information
Me: Remember that we're working on a React app with TypeScript
Claude: [executes brain_remember("current_project", "React app with TypeScript")]

# Recall in a future conversation
Me: What were we working on?
Claude: [executes brain_recall("current_project")]
```

### Code Execution
```
# Run Python code
Me: Can you check if numpy is installed?
Claude: [executes brain_execute("import numpy; print(numpy.__version__)", "python")]

# Run shell commands
Me: What files are in my project directory?
Claude: [executes brain_execute("ls -la ~/Code/my-project", "shell")]
```

### Working with State
```
# Set configuration
Me: Set my preferred editor to VSCode
Claude: [executes state_set("preferred_editor", "VSCode", "config")]

# Track project state
Me: Mark the authentication module as completed
Claude: [executes state_set("auth_module_status", "completed", "project")]
```

## Monitoring Execution

To monitor what Claude is executing in real-time:

1. Start the monitoring server:
   ```bash
   cd monitor
   python server.py
   ```

2. Open the monitoring UI:
   ```
   http://localhost:9996
   ```

This provides full transparency into what commands Claude is running on your system.

## Project Structure

```
claude-brain/
├── index.js          # MCP server (Node.js)
├── package.json      # Node dependencies
├── pyproject.toml    # Python project config
├── monitor/          # Execution monitoring (Python)
│   ├── server.py     # API server
│   └── ui.html       # Web interface
├── data/             # Persistent storage
│   └── brain.db      # SQLite database
├── scripts/          # Utility scripts
└── docs/             # Documentation
```

## Troubleshooting

### Claude doesn't use brain tools automatically
- Make sure you've added the system message to your Claude Desktop user preferences
- Restart Claude Desktop after adding the MCP server configuration
- Try explicitly asking Claude to "initialize the brain session" or "use brain_init"

### "Tool not found" errors
- Verify the MCP server is configured correctly in Claude Desktop
- Check that the path to index.js is absolute, not relative
- Look for errors in Claude Desktop's logs

### Execution not working
- **Check if the execution server is running**: `curl http://localhost:9998/`
- **Start it manually if needed**: `cd ~/Code/mcp-execution-server && uv run python server.py`
- **Check service status**: `launchctl list | grep brain-execution`
- **View logs**: `tail -f ~/Library/Logs/brain-execution-server.log`
- Ensure Node.js is properly installed and in your PATH
- Check that the brain_execute function is not commented out in index.js
- Verify you have appropriate permissions for the commands being executed

## Security Considerations

⚠️ **Important**: Claude Brain gives Claude the ability to execute code on your system. While powerful, use with caution:

- All executions are logged and can be monitored
- You can disable execution by commenting out the `brain_execute` function in `index.js`
- Review the monitoring interface regularly to see what commands have been run
- Only use on systems where you're comfortable with Claude having execution access

## Development

This project uses:
- **Node.js** for the MCP server
- **Python** for monitoring tools
- **SQLite** for persistent storage

## Contributing

Contributions are welcome! Please:
- Fork the repository
- Create a feature branch
- Submit a pull request with a clear description

## License

MIT
