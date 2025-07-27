# Quick Reference

## 🚀 Essential Commands

### Initialize Session
```
brain_init
```

### Store Information
```
brain_remember { "key": "name", "value": "data" }
```

### Search Memories
```
brain_recall { "query": "search term" }
```

### Check Status
```
brain_status { "detailed": true }
```

### Execute Code
```
brain_execute { "code": "print('hello')", "language": "python" }
```

### Create Note
```
obsidian_note { "action": "create", "title": "Title", "content": "..." }
```

### Search Everything
```
unified_search { "query": "term" }
```

### Set State
```
state_set { "key": "key", "value": "value", "category": "session" }
```

### Add Task
```
todo_add { "project": "name", "title": "task" }
```

### Check Reminders
```
check_reminders { "priority": "all" }
```

## 📁 Directory Structure

```
/Core-Documents     - System docs
/Projects          - Project notes
/Daily-Notes       - Daily journal
/Session-Summaries - Work logs
/References        - Knowledge base
/Archive          - Old content
```

## 🔑 Key Concepts

- **Memories**: Persistent storage
- **State**: Categorized data
- **Notes**: Obsidian documents
- **Tasks**: Project todos
- **Reminders**: Important items

## 💡 Tips

1. Start with `brain_init`
2. Use descriptive keys
3. Document decisions
4. Regular reviews
5. Ask for help: `[tool]_help`

## 🆘 Troubleshooting

- **Not initialized**: Run `brain_init`
- **Can't find memory**: Check spelling, use partial search
- **Tool not found**: Check tool name, might need prefix
- **Output too long**: Use `verbose: true`

## 📚 More Help

- Full docs: `Core-Documents/`
- Tool guide: `MCP-Tools-Guide.md`
- Best practices: `Best-Practices.md`
