#!/bin/bash
# Compare old and new Brain systems

echo "🔄 Comparing Brain Systems"
echo "========================="
echo

# Check database sizes
echo "📊 Database Comparison:"
OLD_DB="/Users/bard/Code/brain/data/brain.db"
NEW_DB="/Users/bard/Code/claude-brain/data/brain/brain.db"

if [ -f "$OLD_DB" ]; then
    OLD_SIZE=$(du -h "$OLD_DB" | cut -f1)
    echo "   Old system DB: $OLD_SIZE"
else
    echo "   Old system DB: Not found"
fi

if [ -f "$NEW_DB" ]; then
    NEW_SIZE=$(du -h "$NEW_DB" | cut -f1)
    echo "   New system DB: $NEW_SIZE"
else
    echo "   New system DB: Not yet created"
fi

echo
echo "📁 Directory Structure:"
echo "   Old: /Users/bard/Code/brain ($(du -sh /Users/bard/Code/brain 2>/dev/null | cut -f1))"
echo "   Old: /Users/bard/Code/brain-unified ($(du -sh /Users/bard/Code/brain-unified 2>/dev/null | cut -f1))"
echo "   New: /Users/bard/Code/claude-brain ($(du -sh /Users/bard/Code/claude-brain 2>/dev/null | cut -f1))"

echo
echo "🔧 Service Status:"
echo "   Monitoring API (9998): $(lsof -i :9998 > /dev/null 2>&1 && echo "Running" || echo "Stopped")"
echo "   Monitoring UI (9996): $(lsof -i :9996 > /dev/null 2>&1 && echo "Running" || echo "Stopped")"

echo
echo "💡 Ready to test in Claude:"
echo "1. Keep current brain-unified running"
echo "2. Add claude-brain as a second MCP server"
echo "3. Test both work simultaneously"
echo "4. Compare responses"
