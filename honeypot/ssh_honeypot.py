import socket
import threading
import logging
from config import BIND_HOST, SSH_PORT
from core.db import log_security_event, log_credential
from core.rules import analyze_ssh_login
from core.enricher import enrich_and_record_ip, send_alert
logger = logging.getLogger("ThreatSentinel.SSH")
SSH_BANNER = b"SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.4\r\n"
def handle_ssh_client(client_socket: socket.socket, client_address: tuple):
    client_ip, client_port = client_address
    logger.info(f"[{client_ip}] Incoming SSH/Terminal decoy connection from port {client_port}")
    try:
        client_socket.settimeout(10.0)
        # Send fake OpenSSH banner
        client_socket.sendall(SSH_BANNER)
        # Receive attacker's SSH identification string or probe
        data = client_socket.recv(1024)
        raw_probe = data.decode("utf-8", errors="ignore").strip()
        mitre_tech, mitre_tactic, severity, description = analyze_ssh_login("unknown", "unknown")
        event = {
            "source_ip": client_ip,
            "source_port": client_port,
            "destination_port": SSH_PORT,
            "protocol": "SSH",
            "endpoint": "SSH_HANDSHAKE",
            "method": "CONNECT",
            "payload": raw_probe[:500] if raw_probe else "SSH_BANNER_PROBE",
            "user_agent": raw_probe[:100] if raw_probe else "SSH-Client",
