#!/bin/bash
set -e

echo "🧠 Claude Brain Installation"
echo "=========================="
echo

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed"
    echo "   Install from: https://nodejs.org"
    exit 1
fi

# Check uv (optional)
if command -v uv &> /dev/null; then
    echo "✅ uv found, installing Python dependencies..."
    uv pip install -e ".[monitor]"
else
    echo "⚠️  uv not found, skipping Python dependencies"
    echo "   Monitor features will not be available"
fi

# Install Node dependencies
echo "📦 Installing Node.js dependencies..."
npm install

# Create data directory
mkdir -p data logs

echo
echo "✅ Installation complete!"
echo
echo "Next steps:"
echo "1. Add to Claude Desktop config:"
echo "   $(pwd)/index.js"
echo "2. Start using Brain tools in Claude!"
