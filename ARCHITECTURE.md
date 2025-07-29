# Claude Brain Architecture

## Overview

Claude Brain provides persistent memory and code execution capabilities to Claude Desktop through the Model Context Protocol (MCP). The system consists of a single Node.js MCP server with built-in execution capabilities.

## System Components

### Brain MCP Server
- **Location**: `/Users/bard/Code/claude-brain/index.js`
- **Protocol**: MCP (Model Context Protocol) with Claude Desktop
- **Execution**: Direct subprocess via Node.js `child_process`
- **Storage**: SQLite database at `data/brain.db`
- **Optional Monitoring**: Web UI server on port 9996

### Core Capabilities
- **Memory Operations**: Store and search persistent memories
- **Code Execution**: Run Python and Shell code via subprocess
- **Obsidian Integration**: Read/write notes in Obsidian vault
- **State Management**: Persistent key-value storage

## Data Flow

### Memory Operations
1. `brain_remember(key, value)` → SQLite storage with full-text search
2. `brain_recall(query)` → SQLite FTS search → ranked results
3. `unified_search(query)` → searches both Brain memory and Obsidian notes

### Code Execution
1. Claude calls `brain_execute(code, language)`
2. MCP server validates and spawns subprocess:
   - Python: `spawn('python3', ['-c', code])`
   - Shell: `spawn('sh', ['-c', code])`
3. Captures stdout/stderr with 30-second timeout
4. Returns structured result: `{stdout, stderr, returncode, duration}`

### Obsidian Integration
1. `obsidian_note(action, ...)` → file operations in vault
2. Supports create, read, update, delete, list operations
3. Maintains metadata and folder structure

## Key Functions

### Memory Management
- `brain_init()` - Initialize session and load context
- `brain_remember(key, value, type)` - Store persistent memory
- `brain_recall(query, limit)` - Search memories with FTS
- `brain_status()` - System health and statistics

### Execution System
- `brain_execute(code, description, language)` - Run code safely
- Direct subprocess spawning with timeout enforcement
- Real-time output capture and error handling
- Execution logging for audit trail

### State Operations
- `state_set(key, value, category)` - Store state data
- `state_get(key, category)` - Retrieve state data
- `state_transaction(operations)` - Atomic multi-operations
- Categories: system, project, config, cache, session

### Obsidian Tools
- `obsidian_note(action, identifier, content)` - Note operations
- `unified_search(query, source)` - Cross-system search
- Automatic metadata handling and folder organization

## File System Layout

```
/Users/bard/Code/claude-brain/
├── index.js                 # MCP server entry point
├── package.json             # Node.js dependencies
├── data/
│   └── brain.db            # SQLite database (memories, state, notes)
├── monitor/                 # Optional monitoring
│   ├── server.py           # Web UI server (port 9996)
│   └── ui.html            # Monitoring interface
└── docs/
    ├── README.md
    ├── INSTALLATION.md
    └── ARCHITECTURE.md     # This file
```

## Database Schema

### memories table
- `id` - Auto-increment primary key
- `key` - Memory identifier
- `value` - JSON content
- `type` - Category (general, protocol, etc.)
- `created_at` - Timestamp
- Full-text search enabled

### state table
- `id` - Auto-increment primary key
- `category` - State category (system/project/config/cache/session)
- `key` - State key
- `value` - JSON value
- `updated_at` - Timestamp

### obsidian_notes table
- `id` - Auto-increment primary key
- `path` - Note path in vault
- `title` - Note title
- `content` - Markdown content
- `metadata` - Frontmatter as JSON
- `updated_at` - Timestamp

## Security Model

### Execution Safety
- **Process Isolation**: Each execution runs in separate subprocess
- **Timeout Protection**: 30-second hard limit with SIGTERM/SIGKILL
- **Access Control**: Inherits user permissions, no privilege escalation
- **Resource Limits**: Subprocess-level isolation prevents system impact

### Audit Trail
- All code executions logged with timestamps and results
- Optional web monitoring interface for real-time viewing
- Structured error handling with context preservation
- Database integrity checks available

## Error Handling

### Execution Failures
- Timeout enforcement via process signals
- stderr capture and structured error responses
- Exit code interpretation and user-friendly messages
- Graceful cleanup of failed processes

### System Resilience
- Database connection error recovery
- Graceful degradation when components unavailable
- Comprehensive error logging for diagnostics
- Input validation and sanitization

## Performance Characteristics

### Database Performance
- SQLite with FTS5 for full-text search
- Indexed key fields for fast lookups
- Prepared statements for query efficiency
- Connection pooling for concurrent access

### Execution Performance
- Lightweight subprocess spawning (~10ms overhead)
- Direct output streaming for real-time results
- Minimal memory footprint per execution
- Efficient result serialization

## Maintenance Operations

### Health Monitoring
```bash
# Check MCP server status (via Claude Desktop connection)
# Check optional monitoring server
curl http://localhost:9996/health

# Database integrity
sqlite3 data/brain.db "PRAGMA integrity_check;"
```

### Backup Strategy
- **Critical**: `data/brain.db` (all memories and state)
- **Configuration**: Claude Desktop MCP settings
- **Optional**: Obsidian vault (if using integration)

### Log Management
- Execution logs stored in database
- Optional file logging via monitoring server
- Automatic cleanup of old execution records

## Integration Details

### MCP Protocol Implementation
- JSON-RPC style tool exposure
- Async request/response with proper error propagation
- Resource cleanup and connection management
- Standard MCP capability negotiation

### Claude Desktop Integration
- Tools appear as native Claude functions
- Transparent error handling and user feedback
- Context preservation across conversation turns
- Session state management

## Future Considerations

### Potential Enhancements
- **Execution**: Container-based isolation, additional language support
- **Memory**: Distributed storage, cloud synchronization
- **Security**: Fine-grained permissions, code signing
- **Performance**: Execution pooling, result caching

### Scalability Options
- Multi-process execution pools for concurrent operations
- Distributed memory backends for large-scale storage
- Remote execution capabilities for resource-intensive tasks
- Multi-user support with proper isolation

## Architecture Principles

This design prioritizes:
- **Simplicity**: Single-process design with minimal dependencies
- **Reliability**: Robust error handling and process management
- **Security**: Process isolation and timeout protection
- **Maintainability**: Clear interfaces and comprehensive logging
- **Performance**: Efficient database usage and lightweight execution

The architecture enables persistent memory and safe code execution for Claude Desktop while maintaining system stability through direct integration rather than complex distributed services.
