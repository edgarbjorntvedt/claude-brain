#!/bin/bash
# Comprehensive test suite for claude-brain

set -e

echo "🧪 Claude Brain Test Suite"
echo "========================="
echo

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test counter
TESTS_PASSED=0
TESTS_FAILED=0

# Test function
run_test() {
    local test_name=$1
    local test_cmd=$2
    
    echo -n "Testing $test_name... "
    if eval "$test_cmd" > /tmp/test_output.log 2>&1; then
        echo -e "${GREEN}✓ PASSED${NC}"
        ((TESTS_PASSED++))
    else
        echo -e "${RED}✗ FAILED${NC}"
        echo "  Error output:"
        cat /tmp/test_output.log | head -5 | sed 's/^/    /'
        ((TESTS_FAILED++))
    fi
}

# 1. Test Node.js environment
run_test "Node.js version" "node --version | grep -E 'v(18|20|22|24)'"

# 2. Test dependencies
run_test "Dependencies installed" "test -d node_modules"
run_test "Better-sqlite3" "test -f node_modules/better-sqlite3/lib/index.js"
run_test "MCP SDK" "test -d node_modules/@modelcontextprotocol"

# 3. Test file structure
run_test "index.js exists" "test -f index.js"
run_test "config.js exists" "test -f config.js"
run_test "Data directory" "test -d data/brain"
run_test "Logs directory" "test -d data/logs/execution"

# 4. Test server startup (without hanging)
run_test "Server syntax" "node --check index.js"

# 5. Test database access
cat > test-db.js << 'EOJS'
import Database from 'better-sqlite3';
import { CONFIG } from './config.js';

try {
    const db = new Database(CONFIG.BRAIN_DB_PATH);
    db.prepare('SELECT 1').get();
    db.close();
    process.exit(0);
} catch (e) {
    console.error(e);
    process.exit(1);
}
EOJS

run_test "Database access" "node test-db.js"
rm -f test-db.js

# 6. Test monitoring components
run_test "Monitor server.py" "test -f monitor/server.py"
run_test "Monitor UI" "test -f monitor/ui.html"
run_test "Python syntax" "python3 -m py_compile monitor/server.py"

# Summary
echo
echo "==============================="
echo "Test Results:"
echo "  Passed: $TESTS_PASSED"
echo "  Failed: $TESTS_FAILED"
echo

if [ $TESTS_FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ All tests passed!${NC}"
    echo "The system appears ready for testing with Claude"
else
    echo -e "${RED}❌ Some tests failed${NC}"
    echo "Please fix the issues before proceeding"
fi

# Cleanup
rm -f /tmp/test_output.log
