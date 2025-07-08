#!/bin/bash
# Brain MCP Server LaunchAgent Management Script

PLIST_NAME="com.bard.brain-mcp-server"
PLIST_FILE="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"
SOURCE_PLIST="$(dirname "$0")/${PLIST_NAME}.plist"

case "$1" in
    install)
        echo "Installing Brain MCP Server LaunchAgent..."
        cp "$SOURCE_PLIST" "$PLIST_FILE"
        launchctl load "$PLIST_FILE"
        echo "✓ Installed and started"
        ;;
    
    uninstall)
        echo "Uninstalling Brain MCP Server LaunchAgent..."
        launchctl unload "$PLIST_FILE" 2>/dev/null
        rm -f "$PLIST_FILE"
        echo "✓ Uninstalled"
        ;;
    
    start)
        echo "Starting Brain MCP Server..."
        launchctl load "$PLIST_FILE"
        echo "✓ Started"
        ;;
    
    stop)
        echo "Stopping Brain MCP Server..."
        launchctl unload "$PLIST_FILE"
        echo "✓ Stopped"
        ;;
    
    restart)
        echo "Restarting Brain MCP Server..."
        launchctl kickstart -k "gui/$(id -u)/${PLIST_NAME}"
        echo "✓ Restarted"
        ;;
    
    status)
        echo "Brain MCP Server status:"
        launchctl list | grep "$PLIST_NAME" || echo "Not running"
        ;;
    
    logs)
        echo "=== Recent output logs ==="
        tail -20 "$HOME/Library/Logs/Claude/brain-mcp-server.log"
        echo -e "\n=== Recent error logs ==="
        tail -20 "$HOME/Library/Logs/Claude/brain-mcp-server.error.log"
        ;;
    
    *)
        echo "Usage: $0 {install|uninstall|start|stop|restart|status|logs}"
        exit 1
        ;;
esac
