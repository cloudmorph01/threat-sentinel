import sqlite3
import threading
from datetime import datetime
from typing import Dict, Any, List, Optional
from config import DB_PATH
_local = threading.local()
def get_connection() -> sqlite3.Connection:
    """Thread-safe SQLite connection manager."""
    if not hasattr(_local, "connection") or _local.connection is None:
        _local.connection = sqlite3.connect(
            DB_PATH,
            check_same_thread=False,
            timeout=10.0
        )
        _local.connection.row_factory = sqlite3.Row
    return _local.connection
def init_db():
    """Initializes the database schema and indexes."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS security_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        source_ip TEXT NOT NULL,
        source_port INTEGER,
        destination_port INTEGER NOT NULL,
        protocol TEXT NOT NULL,
        endpoint TEXT,
        method TEXT,
        payload TEXT,
        user_agent TEXT,
        mitre_technique TEXT,
        mitre_tactic TEXT,
        severity TEXT DEFAULT 'INFO',
        details TEXT
