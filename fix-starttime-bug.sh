#!/bin/bash
# Source the path configuration
source "$(dirname "$0")/paths.sh"
# Fix for brain_execute startTime bug
# This script patches the index.js file to fix the startTime scope issue

# Create backup
cp "$CLAUDE_BRAIN_INDEX" "$CLAUDE_BRAIN_INDEX".backup-$(date +%Y%m%d-%H%M%S)

# Apply the fix using sed
# We need to move startTime declaration before the try block
sed -i.bak '
/handler: async ({ code, language = .auto., description }) => {/,/} catch (error) {/ {
  s/let execId, logEntry;/let execId, logEntry, startTime;/
  s/const startTime = Date.now();/startTime = Date.now();/
}' "$CLAUDE_BRAIN_INDEX"

echo "Fix applied! The startTime variable is now declared in the proper scope."
echo "A backup was created with timestamp."
