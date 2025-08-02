#!/usr/bin/env node
import Database from 'better-sqlite3';
import { CONFIG } from '../config.js';
import { fileURLToPath } from 'url';
import { dirname } from 'path';
import  fs from  'fs';
import  path from  'path'

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

console.log('🧪 Testing Brain Core Functions\n');

// Test 1: Database initialization
console.log('1. Testing database initialization...');
try {
    const db = new Database(CONFIG.BRAIN_DB_PATH);
    
    // Check if memories table exists
    const tables = db.prepare("SELECT name FROM sqlite_master WHERE type='table'").all();
    const hasMemoriesTable = tables.some(t => t.name === 'memories');
    
    if (hasMemoriesTable) {
        console.log('   ✅ Memories table exists');
    } else {
        console.log('   ⚠️  Memories table not found - will be created on first use');
    }
    
    db.close();
} catch (e) {
    console.error('   ❌ Database error:', e.message);
}

// Test 2: Memory operations simulation
console.log('\n2. Testing memory operations...');
try {
    const db = new Database(CONFIG.BRAIN_DB_PATH);
    
    // Create table if needed (simulating what brain_init does)
    db.exec(`
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT UNIQUE NOT NULL,
            value TEXT NOT NULL,
            type TEXT DEFAULT 'general',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            accessed_at TEXT DEFAULT CURRENT_TIMESTAMP,
            metadata TEXT DEFAULT '{}'
        )
    `);
    
    // Test store
    const testKey = 'test_' + Date.now();
    const testValue = JSON.stringify({ test: true, timestamp: new Date().toISOString() });
    
    db.prepare('INSERT OR REPLACE INTO memories (key, value, type) VALUES (?, ?, ?)').run(
        testKey, testValue, 'test'
    );
    console.log('   ✅ Memory store works');
    
    // Test recall
    const result = db.prepare('SELECT * FROM memories WHERE key = ?').get(testKey);
    if (result && result.value === testValue) {
        console.log('   ✅ Memory recall works');
    } else {
        console.log('   ❌ Memory recall failed');
    }
    
    // Clean up
    db.prepare('DELETE FROM memories WHERE key = ?').run(testKey);
    db.close();
} catch (e) {
    console.error('   ❌ Memory operations error:', e.message);
}

// Test 3: Check monitoring setup
console.log('\n3. Testing monitoring setup...');
const monitorFiles = [
    'monitor/server.py',
    'monitor/ui.html'
];

monitorFiles.forEach(file => {
    const fullPath = path.join(dirname(dirname(__filename)), file);
    
    if (fs.existsSync(fullPath)) {
        console.log(`   ✅ ${file} exists`);
    } else {
        console.log(`   ❌ ${file} missing`);
    }
});

console.log('\n✅ Function tests complete');
