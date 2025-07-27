# Best Practices

## 🎯 Core Principles

### 1. Document Everything Important
- Decisions and their reasoning
- Problems and their solutions  
- Patterns you discover
- Useful code snippets

### 2. Use Descriptive Keys
```
# Good
brain_remember { "key": "api_auth_jwt_implementation" }

# Not so good
brain_remember { "key": "thing1" }
```

### 3. Organize with Types and Categories
- Use `type` for memories (project, pattern, general)
- Use categories for state (system, project, session, cache)
- Create consistent folder structures in notes

## 📝 Memory Management

### Storing Memories
1. **Be Specific**: Include context in the value
```json
{
  "key": "deploy_process_prod",
  "value": {
    "steps": ["test", "build", "deploy"],
    "last_updated": "2025-07-27",
    "notes": "Always run tests first"
  }
}
```

2. **Use JSON for Complex Data**: Structured data is easier to search and update

3. **Regular Reviews**: Periodically search and clean old memories

### Searching Effectively
- Use partial matches: `brain_recall { "query": "deploy" }`
- Search in values too: The system searches both keys and values
- Be aware of limits: Default is 10 results, increase if needed

## 📂 Note Organization

### Folder Structure
```
/Projects
  /ProjectName
    - Overview.md
    - Tasks.md
    - Decisions.md
    - Resources.md
/Daily-Notes
  - 2025-07-27.md
/References
  - Tools.md
  - Patterns.md
/Archive
  - [Old projects]
```

### Linking Strategy
- Use [[WikiLinks]] to connect related notes
- Create index notes for major topics
- Tag consistently (#project, #decision, #learning)

## 🔄 Session Management

### Starting Sessions
1. Always run `brain_init` first
2. Review critical reminders
3. Check last project status
4. Plan session goals

### During Sessions
- Save progress regularly with `brain_remember`
- Update task status
- Document decisions immediately
- Create notes for complex topics

### Ending Sessions
- Summarize key accomplishments
- Update project status
- Set reminders for next time
- Clean up temporary state

## 🛠️ Tool Usage

### Choose the Right Tool
- **Quick notes**: Use memories
- **Long content**: Create Obsidian notes
- **Temporary data**: Use state with session/cache category
- **Code execution**: Use brain_execute with clear descriptions

### Combine Tools Effectively
```
# Example: Research workflow
1. web_search { "query": "topic" }
2. brain_remember { "key": "research_topic_sources" }
3. obsidian_note { "action": "create", "title": "Topic Research" }
4. todo_add { "title": "Review research findings" }
```

### Performance Tips
- Use `verbose: false` by default to save context
- Batch operations when possible
- Clean up cache/session state regularly
- Archive old projects

## 🔒 Security & Privacy

### Sensitive Information
- Never store passwords in plain text
- Use generic examples in shared notes
- Keep personal data in separate vaults
- Regular backups of important data

### Sharing Safely
- Review notes before sharing
- Remove personal identifiers
- Use templates for common patterns
- Document publicly shareable content

## 🚀 Advanced Patterns

### Project Templates
Create reusable project structures:
```json
{
  "key": "template_web_project",
  "value": {
    "folders": ["src", "tests", "docs"],
    "files": ["README.md", "package.json"],
    "tasks": ["Setup", "Development", "Testing", "Deploy"]
  }
}
```

### Workflow Automation
Chain tools for complex tasks:
```javascript
// Example: Daily standup automation
1. Get yesterday's completed tasks
2. Get today's planned tasks  
3. Check blockers
4. Generate summary note
5. Set reminders for important items
```

### Knowledge Building
- Create "Today I Learned" notes
- Document error solutions immediately
- Build a personal wiki of patterns
- Regular knowledge reviews

## 💡 Tips for Success

1. **Start Small**: Don't try to organize everything at once
2. **Be Consistent**: Use the same patterns repeatedly
3. **Iterate**: Refine your system as you learn
4. **Backup**: Regular exports of important data
5. **Share**: Document useful patterns for others

## 🎯 Common Pitfalls to Avoid

1. **Over-organizing**: Don't spend more time organizing than doing
2. **Duplicate data**: Choose one source of truth
3. **Stale information**: Regular reviews and updates
4. **Context flooding**: Use output filtering wisely
5. **Tool obsession**: Tools serve you, not vice versa

## 📚 Continuous Improvement

- Weekly reviews of your system
- Monthly cleanup of old data
- Quarterly system improvements
- Share learnings with community

Remember: The best system is the one you actually use!
