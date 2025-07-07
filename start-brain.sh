#!/bin/bash
# Start Claude Brain MCP Server

cd "$(dirname "$0")"
echo "🧠 Starting Claude Brain MCP Server..."
exec node index.js
