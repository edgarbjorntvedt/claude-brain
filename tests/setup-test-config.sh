#!/bin/bash
# Source the path configuration
source "$(dirname "$0")/../paths.sh"
# Setup claude-brain for parallel testing with brain-unified

echo "🔄 Setting up claude-brain for parallel testing"
echo "============================================="
echo

# Copy current database to test location (if you want to test with existing data)
if [ -f ""$BRAIN_LEGACY_DB"" ]; then
    echo "📋 Option 1: Copy existing database for testing? (y/n)"
    read -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp ""$BRAIN_LEGACY_DB"" "./data/brain/brain.db"
        echo "✅ Copied existing database"
    else
        echo "✅ Will start with fresh database"
    fi
else
    echo "ℹ️  No existing database found, starting fresh"
fi

echo
echo "📝 Creating Claude Desktop test configuration..."
echo

# Get current config location
CONFIG_FILE="$HOME/Library/Application Support/Claude/claude_desktop_config.json"

if [ -f "$CONFIG_FILE" ]; then
    echo "Current MCP servers configured:"
    cat "$CONFIG_FILE" | grep -A5 "mcpServers" | head -20
    echo
fi

echo "📋 To test claude-brain alongside brain-unified:"
echo
echo "Add this to your Claude Desktop config:"
echo
cat << 'JSON'
{
  "mcpServers": {
    "brain-unified": {
      "command": "node",
      "args": [""$BRAIN_UNIFIED_INDEX""]
    },
    "claude-brain-test": {
      "command": ""$CLAUDE_BRAIN_START_SCRIPT""
    }
  }
}
JSON

echo
echo "Then in Claude you can test both:"
echo "- Original: Uses 'brain-unified' prefix"  
echo "- New: Uses 'claude-brain-test' prefix"
echo
echo "Example test queries:"
echo "1. brain-unified:brain_status"
echo "2. claude-brain-test:brain_status"
echo "3. Compare the outputs!"
