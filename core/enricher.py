
import ipaddress
import requests
import json
import logging
from typing import Dict, Any
from config import GEOIP_API_URL, ABUSEIPDB_API_KEY, DISCORD_WEBHOOK_URL
from core.db import upsert_ip_intelligence
logger = logging.getLogger("ThreatSentinel.Enricher")
_geo_cache: Dict[str, Dict[str, Any]] = {}
def is_private_ip(ip_str: str) -> bool:
    """Checks if an IP is local, loopback, or private."""
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip.is_private or ip.is_loopback or ip.is_reserved
    except ValueError:
        return True
def get_ip_geo(ip: str) -> Dict[str, Any]:
    """Resolves IP to Geographic metadata via cache or free IP-API."""
    if ip in _geo_cache:
        return _geo_cache[ip]
    if is_private_ip(ip):
        mock_private = {
            "country": "Localhost / Private Net",
            "country_code": "LOC",
            "city": "Internal Lab",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "isp": "Local Private Network"
        }
        _geo_cache[ip] = mock_private
        return mock_private
    try:
        url = GEOIP_API_URL.format(ip=ip)
        resp = requests.get(url, timeout=3.0)
