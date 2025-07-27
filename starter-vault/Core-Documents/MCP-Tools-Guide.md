# MCP Tools Guide

## 🛠️ Available MCP Tools

The Brain system includes 30+ MCP tools that extend Claude's capabilities. Here's a guide to the most useful ones.

## 📊 Core Brain Tools

### brain_init
Initialize your session and load context.
```
brain_init { "reload": false }
```

### brain_remember
Store information persistently.
```
brain_remember {
  "key": "project_status_api",
  "value": { "phase": "development", "progress": 0.6 },
  "type": "project"
}
```

### brain_recall
Search through your memories.
```
brain_recall { "query": "api", "limit": 10 }
```

### brain_status
Check system health and statistics.
```
brain_status { "detailed": true }
```

### brain_execute
Execute Python or Shell code.
```
brain_execute {
  "code": "import datetime; print(datetime.datetime.now())",
  "language": "python",
  "description": "Get current time"
}
```

## 📝 Note Management

### obsidian_note
Create, read, update, or delete notes.
```
obsidian_note {
  "action": "create",
  "title": "Meeting Notes",
  "content": "## Agenda\n- Item 1\n- Item 2"
}
```

### unified_search
Search across both memories and notes.
```
unified_search {
  "query": "project planning",
  "limit": 20,
  "source": "all"
}
```

## 💾 State Management

### state_set / state_get
Manage categorized state data.
```
state_set {
  "key": "current_task",
  "value": "implementing filters",
  "category": "session"
}

state_get {
  "key": "current_task",
  "category": "session"
}
```

## 📋 Project Management

### todo_add / todo_list
Manage tasks across projects.
```
todo_add {
  "project": "my-api",
  "title": "Add authentication",
  "priority": "high"
}

todo_list { "project": "my-api" }
```

### brain_manager tools
Advanced project management and context switching.

## 🎲 Utility Tools

### random tools
Generate random numbers, choices, passwords.
```
random_integer { "min": 1, "max": 100 }
random_password { "length": 16 }
```

### reminders
Set and manage reminders.
```
remind_me {
  "content": "Review API documentation",
  "priority": "high"
}
```

## 🔍 File Operations

### filesystem tools
Read, write, and manage files.
```
read_file { "path": "/path/to/file.txt" }
write_file { 
  "path": "/path/to/new.txt",
  "content": "Hello, World!"
}
```

### smalledit tools
Make quick edits to files.
```
sed_edit {
  "file": "/path/to/file.txt",
  "pattern": "s/old/new/g"
}
```

## 🤖 AI Enhancement

### sequential-thinking
Structured problem-solving tool.
```
sequentialthinking {
  "thought": "Breaking down the problem...",
  "nextThoughtNeeded": true,
  "thoughtNumber": 1,
  "totalThoughts": 5
}
```

### contemplation
Background processing for complex thoughts.

### subconscious
Delegate tasks for deep processing.

## 🌐 External Integration

### web_search
Search the web with tracking.
```
web_search { "query": "latest AI developments" }
```

### vision tools
Analyze screenshots and images.
```
vision_screenshot {
  "prompt": "What's on my screen?"
}
```

## 💡 Best Practices

1. **Start Simple**: Begin with basic brain tools
2. **Combine Tools**: Many tasks benefit from multiple tools
3. **Use Appropriate Tools**: Each tool has its strengths
4. **Document Usage**: Keep notes on useful patterns

## 🔧 Tool Categories

- **Memory**: brain_*, state_*
- **Notes**: obsidian_note, unified_search
- **Projects**: todo_*, brain_manager
- **Files**: filesystem, smalledit
- **Utility**: random, reminders
- **AI**: sequential-thinking, contemplation
- **External**: web_search, vision

## 📚 Learning Resources

1. **Tool Documentation**: Use `[tool]_help` commands
2. **Examples**: This guide includes basic examples
3. **Experimentation**: Try tools in safe environments
4. **Community**: Share patterns and workflows

## 🚀 Advanced Workflows

### Example: Project Setup
```
1. brain_remember { "key": "project_myapp", "value": {...} }
2. todo_add { "project": "myapp", "title": "Initial setup" }
3. obsidian_note { "action": "create", "title": "MyApp Planning" }
4. create_directory { "path": "/Code/myapp" }
```

### Example: Daily Review
```
1. brain_status { "detailed": true }
2. check_reminders { "priority": "all" }
3. todo_list { "status": "open" }
4. unified_search { "query": "yesterday" }
```

Remember: Tools are meant to enhance your workflow, not complicate it. Start with what you need and expand gradually!
