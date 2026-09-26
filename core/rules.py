import re
from typing import Dict, Any, Tuple
# Detection Signatures and MITRE ATT&CK Mapping
RULES = [
    {
        "name": "SQL Injection (SQLi)",
        "pattern": re.compile(
            r"(\b(union(\s+all)?\s+select|select\s+.*\s+from|insert\s+into|drop\s+(table|database)|exec(\s|\+)+(s|x)p\w+)\b|"
            r"(\'|\%27)\s*(or|and)\s*(\'|\%27)?\d+(\'|\%27)?\s*=\s*(\'|\%27)?\d+|"
            r"--|\#|\/\*|\*\/)",
            re.IGNORECASE
        ),
        "mitre_id": "T1190",
        "mitre_technique": "T1190 - Exploit Public-Facing Application",
        "mitre_tactic": "Initial Access",
        "severity": "HIGH",
        "description": "Attempted SQL injection probe targeting backend databases."
    },
    {
        "name": "Path Traversal / Local File Inclusion (LFI)",
        "pattern": re.compile(
            r"(\.\.\/|\.\.\\|%2e%2e%2f|%2e%2e\/|\/etc\/passwd|\/etc\/shadow|c:\\windows\\system32|win\.ini|boot\.ini)",
            re.IGNORECASE
        ),
        "mitre_id": "T1083",
        "mitre_technique": "T1083 - File and Directory Discovery",
        "mitre_tactic": "Discovery",
        "severity": "HIGH",
        "description": "Attempted path traversal to read sensitive host files."
    },
    {
        "name": "Remote Code Execution (RCE) / Shell Injection",
        "pattern": re.compile(
            r"(;\s*(cat|ls|pwd|whoami|id|uname|curl|wget|bash|sh|powershell|cmd\.exe|nc|netcat)\b|"
            r"\|\s*(cat|ls|whoami|id|curl|wget|bash|sh|powershell)\b|"
            r"\$\(.*\)|`.*`|\/bin\/bash|\/bin\/sh)",
