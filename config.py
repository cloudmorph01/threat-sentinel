import os
from pathlib import Path
# Base Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "sentinel.db"
# Server Bind Configuration
BIND_HOST = "0.0.0.0"
# Honeypot Ports
HTTP_PORT = int(os.getenv("SENTINEL_HTTP_PORT", 8080))
SSH_PORT = int(os.getenv("SENTINEL_SSH_PORT", 2222))
# Threat Intelligence & Geolocation
# ip-api.com free endpoint for IP geolocation
GEOIP_API_URL = "http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,lat,lon,isp,org,as,query"
GEOIP_CACHE_TIMEOUT = 86400  # 24 hours in seconds
# Optional Threat Intelligence API Keys (Leave blank to use internal heuristic scoring)
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY", "")
# Optional Alerting (Discord Webhook for instant alerts on CRITICAL severity events)
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")
# Detection Sensitivity
ALERT_SEVERITIES = ["INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
CRITICAL_ALERT_THRESHOLD = "HIGH"
