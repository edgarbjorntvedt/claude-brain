# Claude's System Map: Brain System

## Map Purpose
This is Claude's navigation map for the Brain system - not human documentation. Optimized for quick file location, system understanding, and operational efficiency.

## System Overview
**Primary Function**: Persistent memory and code execution for Claude Desktop via MCP protocol
**Core Location**: `/Users/bard/Code/claude-brain/`
**Database**: `data/brain.db` (SQLite with FTS)
**Integration**: Direct MCP connection to Claude Desktop
**Obsidian Vault**: `/Users/bard/Code/claude-brain/data/BrainVault/` ✅ VERIFIED

## File Map

### Primary Files
- **`index.js`** - Main MCP server, all core functions
- **`package.json`** - Dependencies and scripts  
- **`data/brain.db`** - SQLite database (memories, state, notes)
- **`data/BrainVault/`** - Obsidian vault location ✅ CORRECTED 2025-07-29
- **`MAP.md`** - This navigation file

### Optional Components
- **`monitor/server.py`** - Web UI (port 9996) 
- **`monitor/ui.html`** - Monitoring interface

## System Status Updates (2025-07-29)

### ✅ Major Fixes Completed
- **Tools Registry Fixed**: No longer reports false "broken" status for working tools
- **Architecture Paths Corrected**: Obsidian vault path updated in all documentation
- **sed_edit Quoting Issue**: Diagnosed - use pipe `|` delimiter for paths instead of `/`
- **ELVIS Integration**: Verified working after restart
- **Living Architecture Protocol**: Verified functional

### 🔧 Tools Registry Status
**Working Tools Previously Misreported**: mcp-project-finder, mcp-protocol-tracker, mcp-tracked-search, mcp-subconscious, mcp-tool-tracker, mcp-vision
**Registry Logic**: Now checks actual package.json main entry instead of hardcoded dist/index.js

### 🚫 Known Issues
- **sed_edit patterns**: Use `s|old/path|new/path|g` not `s/old/path/new/path/g` for paths
- **Only broken tool**: mcp-test-documentation (legitimate - missing package.json)

## Function Map

### Memory Operations
- `brain_init()` → Initialize session, load context
- `brain_remember(key, value, type)` → Store in SQLite with FTS
- `brain_recall(query, limit)` → Search memories, return ranked results
- `brain_status()` → System health and statistics

### Code Execution  
- `brain_execute(code, description, language)` → Direct subprocess execution
  - Python: `spawn('python3', ['-c', code])`
  - Shell: `spawn('sh', ['-c', code])`
  - 30-second timeout, structured result format

### State Management
- `state_set(key, value, category)` → Store persistent state
- `state_get(key, category)` → Retrieve state data
- `state_transaction(operations)` → Atomic multi-operations
- Categories: system, project, config, cache, session

### Obsidian Integration
- `obsidian_note(action, identifier, content)` → Note operations
- `unified_search(query, source)` → Cross-system search
- Auto-handles metadata and folder structure

## Data Flow Map

### Memory: `Claude → brain_remember() → SQLite FTS → stored`
### Recall: `Claude → brain_recall() → SQLite search → ranked results`  
### Execute: `Claude → brain_execute() → child_process.spawn() → subprocess → results`
### State: `Claude → state_set() → SQLite → persistent storage`

## Database Map

### Tables
- **memories**: `{id, key, value, type, created_at}` + FTS index
- **state**: `{id, category, key, value, updated_at}`
- **obsidian_notes**: `{id, path, title, content, metadata, updated_at}`

## Integration Map

### MCP Protocol
- **Connection**: stdio with Claude Desktop
- **Tools**: Exposed as native Claude functions
- **Error handling**: Structured responses with context
- **State**: No global variables, database-only persistence

### Execution Engine
- **Method**: Direct Node.js child_process (no separate server)
- **Isolation**: Per-subprocess, clean environment
- **Security**: User permissions, 30s timeout, signal termination
- **Output**: Real-time stdout/stderr capture

## Quick Reference

### File Locations
```
/Users/bard/Code/claude-brain/
├── index.js              # Main server (all functions)
├── data/brain.db         # SQLite database  
├── monitor/server.py     # Optional web UI
└── MAP.md               # This file
```

### Key Commands
- **Search files**: `locate filename` (uses ~/.locatedb)
- **Manual DB update**: `~/bin/update-locate-db.sh`
- **Health check**: Via brain_status() function
- **Database check**: `sqlite3 data/brain.db "PRAGMA integrity_check;"`

### System Dependencies
- **Node.js**: MCP server runtime
- **SQLite**: Database engine with FTS5
- **Python3**: For subprocess execution
- **GNU locate**: User file database (cron updated)

## Operational Notes

### Performance
- SQLite FTS5 for fast memory search
- Lightweight subprocess spawning (~10ms overhead)
- Connection pooling for database efficiency
- Direct output streaming for real-time results

### Maintenance  
- **Critical backup**: `data/brain.db`
- **Locate updates**: Daily 5 AM via cron
- **Log monitoring**: Via optional web UI
- **Health checks**: Built into brain_status()

### Security Model
- **Execution**: User permissions only, no escalation
- **Timeouts**: 30s hard limit with SIGTERM/SIGKILL  
- **Isolation**: Separate subprocess per execution
- **Audit**: All operations logged with timestamps

## Navigation Strategy
1. **Check this map first** for file locations and system understanding
2. **Use locate** for quick filename searches (updated daily)  
3. **Use find** only as last resort for complex searches

This map eliminates the need for file hunting and provides immediate system navigation for operational efficiency.
