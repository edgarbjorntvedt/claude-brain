#!/bin/bash
# Configuration for Claude Brain shell scripts
# Source this file to get portable path variables

# Get the directory where this script is located (project root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# === PROJECT PATHS ===
export CLAUDE_BRAIN_ROOT="$SCRIPT_DIR"
export CLAUDE_BRAIN_DATA="$SCRIPT_DIR/data"
export CLAUDE_BRAIN_LOGS="$SCRIPT_DIR/data/logs"
export CLAUDE_BRAIN_VAULT="$SCRIPT_DIR/data/BrainVault"

# === SISTER PROJECT PATHS ===
export GITHUB_ROOT="$(dirname "$SCRIPT_DIR")"
export BRAIN_LEGACY="$GITHUB_ROOT/brain"
export BRAIN_UNIFIED="$GITHUB_ROOT/brain-unified"
export MCP_EXECUTION_SERVER="$GITHUB_ROOT/mcp-execution-server"
export MCP_MERCURY_EVOLUTION="$GITHUB_ROOT/mcp-mercury-evolution"

# === COMPUTED PATHS ===
export BRAIN_LEGACY_DB="$BRAIN_LEGACY/data/brain.db"
export BRAIN_UNIFIED_INDEX="$BRAIN_UNIFIED/index.js"
export CLAUDE_BRAIN_INDEX="$CLAUDE_BRAIN_ROOT/index.js"
export CLAUDE_BRAIN_START_SCRIPT="$CLAUDE_BRAIN_ROOT/start-brain.sh"

# === USER PATHS ===
export USER_HOME="$HOME"
export USER_LIBRARY_LOGS="$HOME/Library/Logs"

# Debug function to show all paths
debug_paths() {
    echo "=== Claude Brain Shell Configuration ==="
    echo "CLAUDE_BRAIN_ROOT: $CLAUDE_BRAIN_ROOT"
    echo "GITHUB_ROOT: $GITHUB_ROOT"
    echo "BRAIN_LEGACY: $BRAIN_LEGACY"
    echo "BRAIN_UNIFIED: $BRAIN_UNIFIED"
    echo "CLAUDE_BRAIN_INDEX: $CLAUDE_BRAIN_INDEX"
    echo "========================================"
}
