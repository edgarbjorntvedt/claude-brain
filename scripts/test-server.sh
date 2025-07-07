#!/bin/bash
echo "🧪 Testing Claude Brain MCP Server..."
echo

# Test that the server can start
timeout 5s node index.js < /dev/null

if [ $? -eq 124 ]; then
    echo "✅ Server started successfully (timed out as expected for stdio server)"
else
    echo "❌ Server failed to start"
    exit 1
fi

echo
echo "✅ Basic server test passed!"
echo "The MCP server is ready to be configured in Claude Desktop"
