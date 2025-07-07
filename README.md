# Claude Brain 🧠

A unified, clean, and simple persistent memory system for Claude via MCP (Model Context Protocol).

## Overview

Claude Brain provides Claude with persistent memory across conversations, combining the best features from previous implementations into a single, maintainable codebase.

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

2. **Configure Claude Desktop**:
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

3. **Start using**:
   - `brain_init` - Initialize your session
   - `brain_remember` - Store information
   - `brain_recall` - Search memories
   - `brain_status` - Check system status

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

## Development

This project uses:
- **uv** for Python dependency management
- **Node.js** for the MCP server
- **SQLite** for persistent storage

## License

MIT
