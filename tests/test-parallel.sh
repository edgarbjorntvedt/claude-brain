#!/bin/bash
# Test claude-brain in parallel with existing system

echo "🔄 Setting up parallel test environment..."
echo

# Create a test database (separate from production)
export TEST_DB_PATH="./data/brain/brain_test.db"
export TEST_LOG_DIR="./data/logs/test_execution"

mkdir -p "$(dirname $TEST_DB_PATH)"
mkdir -p "$TEST_LOG_DIR"

# Create a test config
cat > config.test.js << EOJS
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export const CONFIG = {
  BRAIN_DB_PATH: join(__dirname, 'data/brain/brain_test.db'),
  LOG_DIR: join(__dirname, 'data/logs/test_execution'),
  VAULT_PATH: join(__dirname, 'data/vault_test'),
  MONITOR_PORT: 9996,  // Same as production for now
  API_PORT: 9998       // Same as production for now
};
EOJS

echo "✅ Test environment created"
echo
echo "🧪 Running server with test config..."
echo "(Press Ctrl+C to stop)"
echo

# Run with test config (this will wait for input)
node --input-type=module -e "
import('./config.test.js').then(module => {
  global.CONFIG = module.CONFIG;
  return import('./index.js');
});
"
