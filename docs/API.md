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
Smart search through stored memories.
- `query`: Search terms or phrase
- `limit`: Maximum results (default: 10)
- `mode`: Search strategy (default: "balanced")
  - `balanced`: Equal weight to keys and content
  - `title-focused`: Prioritize memory keys/titles
  - `content-focused`: Search mainly in content
  - `recent`: Show recent matches first
  - `exact`: Exact phrase matching

**Examples:**
```json
// Basic search
{ "query": "API project" }

// Find by title/key
{ "query": "database", "mode": "title-focused" }

// Search content
{ "query": "implementation", "mode": "content-focused" }

// Recent mentions
{ "query": "bug", "mode": "recent" }

// Exact phrase
{ "query": "error handling", "mode": "exact" }
```

**Features:**
- Relevance scoring for better results
- Full-text search with automatic fallback
- Search modes for different use cases

### brain_status
Check system status and statistics.

### brain_execute
Execute Python or shell code with full system access.
- `code`: Code to execute
- `language`: python/shell/auto
- `description`: What this code does

## Monitoring

Access the execution monitor at: http://localhost:9996/
