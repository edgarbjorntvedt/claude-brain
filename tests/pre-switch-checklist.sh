#!/bin/bash
# Pre-switch checklist

echo "🔍 Claude Brain Pre-Switch Checklist"
echo "===================================="
echo

CHECKS_PASSED=0
CHECKS_FAILED=0

check() {
    local name=$1
    local cmd=$2
    
    echo -n "[ ] $name... "
    if eval "$cmd" > /dev/null 2>&1; then
        echo "✅"
        ((CHECKS_PASSED++))
    else
        echo "❌"
        ((CHECKS_FAILED++))
    fi
}

echo "Core Systems:"
check "Node modules installed" "test -d node_modules"
check "Database directory exists" "test -d data/brain"
check "Config file exists" "test -f config.js"
check "Start script executable" "test -x start-brain.sh"

echo
echo "Brain Tools:"
check "Index.js valid" "node --check index.js 2>/dev/null"
check "Has brain_init tool" "grep -q brain_init index.js"
check "Has brain_remember tool" "grep -q brain_remember index.js"
check "Has brain_recall tool" "grep -q brain_recall index.js"
check "Has brain_execute tool" "grep -q brain_execute index.js"

echo
echo "Monitoring System:"
check "Monitor server exists" "test -f monitor/server.py"
check "Monitor UI exists" "test -f monitor/ui.html"
check "Management script exists" "test -f scripts/manage.sh"

echo
echo "===================================="
echo "Results: $CHECKS_PASSED passed, $CHECKS_FAILED failed"
echo

if [ $CHECKS_FAILED -eq 0 ]; then
    echo "✅ System appears ready for switch!"
    echo
    echo "Recommended test procedure:"
    echo "1. Run: ./scripts/setup-test-config.sh"
    echo "2. Configure Claude Desktop with both servers"
    echo "3. Test both in parallel"
    echo "4. Verify all functions work"
    echo "5. Switch when confident"
else
    echo "❌ Please fix failed checks before switching"
fi
