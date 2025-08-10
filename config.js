import { join } from 'path';
import * as os from 'os';

const dataDir = process.env.BRAIN_DATA_PATH || join(os.homedir(), '.claude-brain', 'brain');

export const CONFIG = {
  PYTHON_PATH: '/usr/bin/python3', // some uses /usr/local/bin/python3, Used for direct code execution via child_process
  BRAIN_DB_PATH: join(dataDir, 'brain/brain.db'),
  LOG_DIR: join(dataDir, 'logs/execution'),
  VAULT_PATH: join(dataDir, 'BrainVault'),
  MONITOR_PORT: 9996
};
