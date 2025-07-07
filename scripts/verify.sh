#!/bin/bash
echo "🔍 Verifying claude-brain setup..."
echo

# Check Node version
node_version=$(node --version)
echo "Node.js: $node_version"

# Check if main files exist
files=("index.js" "package.json" "config.js")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ $file missing"
    fi
done

# Check directories
dirs=("data/brain" "data/logs/execution" "monitor" "scripts")
for dir in "${dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir/ exists"
    else
        echo "❌ $dir/ missing"
    fi
done

echo
echo "Run 'npm install' to install dependencies"
