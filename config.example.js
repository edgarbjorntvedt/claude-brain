// File: /home/edgar/github/claude-brain/config.example.js
// Purpose: Example configuration file for Claude Brain

import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

export const CONFIG = {
  // Database location
  BRAIN_DB_PATH: join(__dirname, 'data/brain/brain.db'),
  
  // Execution logs directory
  LOG_DIR: join(__dirname, 'data/logs/execution'),
  
  // Obsidian vault location (if using Obsidian integration)
  VAULT_PATH: join(__dirname, 'data/vault'),
  
  // Monitoring ports
  MONITOR_PORT: 9996,
  API_PORT: 9998
};
