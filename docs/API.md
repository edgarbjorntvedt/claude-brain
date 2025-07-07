# Claude Brain API Documentation

## Core Tools

### brain_init
Initialize a Brain session and load user context.

### brain_remember
Store information in persistent memory.
- `key`: Unique identifier
- `value`: Information to store
- `type`: Category (general, project, pattern)

### brain_recall
Search through stored memories.
- `query`: Search terms
- `limit`: Maximum results (default: 10)

### brain_status
Check system status and statistics.

### brain_execute
Execute Python or shell code with full system access.
- `code`: Code to execute
- `language`: python/shell/auto
- `description`: What this code does

## Monitoring

Access the execution monitor at: http://localhost:9996/
