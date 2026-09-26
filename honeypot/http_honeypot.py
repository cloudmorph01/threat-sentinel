
import http.server
import socketserver
import urllib.parse
import json
import logging
from typing import Tuple
from config import BIND_HOST, HTTP_PORT
from core.db import log_security_event, log_credential
from core.rules import analyze_request
from core.enricher import enrich_and_record_ip, send_alert
logger = logging.getLogger("ThreatSentinel.HTTP")
LOGIN_PAGE_HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Internal Corp Portal - Authentication</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #1e293b; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.5); width: 340px; border: 1px solid #334155; }
        h2 { margin-top: 0; color: #38bdf8; font-size: 1.3rem; }
        input[type="text"], input[type="password"] { width: 100%; padding: 10px; margin: 8px 0 16px 0; border: 1px solid #475569; border-radius: 4px; background: #0f172a; color: white; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #0284c7; color: white; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; }
        button:hover { background: #0369a1; }
        .badge { font-size: 0.75rem; color: #94a3b8; margin-top: 15px; text-align: center; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Corporate Gateway</h2>
        <form method="POST" action="/login">
            <label>Username / Email</label>
