# Boot Sequence

This document describes the initialization sequence for the Brain system.

## 🚀 Standard Boot Sequence

1. **Run brain_init**
   ```
   brain_init
   ```
   This initializes your session and loads basic context.

2. **Check for Critical Reminders**
   The system will display any critical reminders that need attention.

3. **Load Recent Context**
   - The system loads your recent memories
   - Previous session context is restored
   - Active projects are identified

4. **Review System Status**
   ```
   brain_status { "detailed": true }
   ```

## 📋 First-Time Setup

If this is your first time using the Brain system:

1. **Set Your Preferences**
   - Copy `User-Preferences-Template.md` to `User-Preferences.md`
   - Customize it with your information

2. **Create Your First Memory**
   ```
   brain_remember {
     "key": "system_initialized",
     "value": {
       "date": "2025-07-27",
       "user": "your-name"
     }
   }
   ```

3. **Test the Search Function**
   ```
   brain_recall { "query": "system" }
   ```

## 🔄 Session Management

### Starting a New Session
- Always run `brain_init` at the start
- Review any critical reminders
- Check your last project status

### Ending a Session
- Save important progress with `brain_remember`
- Update project status if needed
- Document any important decisions

## 🛠️ Troubleshooting

If initialization fails:
1. Check that the Brain service is running
2. Verify your configuration is correct
3. Check the logs in `~/Library/Logs/Claude/`

## 📚 Next Steps

After successful initialization:
- Read the [System Overview](System-Overview.md)
- Explore available [MCP Tools](MCP-Tools-Guide.md)
- Start building your knowledge base!
