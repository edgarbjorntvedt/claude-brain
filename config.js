import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export const CONFIG = {
  PYTHON_PATH: '/usr/bin/python3', // some uses /usr/local/bin/python3, Used for direct code execution via child_process
  BRAIN_DB_PATH: join(__dirname, 'data/brain/brain.db'),
  LOG_DIR: join(__dirname, 'data/logs/execution'),
  VAULT_PATH: join(__dirname, 'data/BrainVault'),
  MONITOR_PORT: 9996
};
