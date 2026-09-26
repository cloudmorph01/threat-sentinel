import threading
import time
import sys
import logging
import signal
from pathlib import Path
# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("ThreatSentinel.Master")
from config import HTTP_PORT, SSH_PORT, BIND_HOST, DB_PATH
from core.db import init_db
from honeypot.http_honeypot import start_http_honeypot
from honeypot.ssh_honeypot import start_ssh_honeypot
def banner():
    print(r"""
  _______ _                    _    _____            _   _            _ 
 |__   __| |                  | |  / ____|          | | (_)          | |
    | |  | |__  _ __ ___  __ _| |_| (___   ___ _ __ | |_ _ _ __   ___| |
    | |  | '_ \| '__/ _ \/ _` | __|\___ \ / _ \ '_ \| __| | '_ \ / _ \ |
    | |  | | | | | |  __/ (_| | |_ ____) |  __/ | | | |_| | | | |  __/ |
    |_|  |_| |_|_|  \___|\__,_|\__|_____/ \___|_| |_|\__|_|_| |_|\___|_|
                                v1.0.0 (Mini-SIEM & Deception Platform)
    """)
    print("=" * 72)
    print(f" [✓] Database Initialized: {DB_PATH}")
    print(f" [✓] HTTP Decoy Honeypot : http://{BIND_HOST}:{HTTP_PORT} (Trapping /admin, .env, SQLi, LFI)")
    print(f" [✓] SSH Decoy Listener  : {BIND_HOST}:{SSH_PORT} (Trapping credential brute force)")
    print(f" [✓] Threat Intel Engine : Enabled (GeoIP + Heuristic Scoring)")
    print("=" * 72)
