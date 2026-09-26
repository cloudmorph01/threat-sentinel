🛡️ ThreatSentinel: Intelligent Honeypot & Mini-SIEM Platform
ThreatSentinel is a modular, lightweight Cybersecurity Deception & Security Operations Center (SOC) telemetry platform. It deploys decoy services (HTTP and SSH/Telnet), traps malicious bots and human adversaries in real time, normalizes threat data, maps attack patterns to the MITRE ATT&CK Framework, enriches telemetry with GeoIP & threat intelligence, and presents an interactive SOC Analyst Dashboard.

🌟 Key Highlights & Architecture
🍯 Multi-Protocol Honeypots:
HTTP Decoy (:8080): Simulates administrative logins (/admin, /login), intercepts directory traversal (/etc/passwd), SQL injection probes, and credential sniffing (.env, .git/config, wp-config.php).
SSH/Telnet Decoy (:2222): Traps automated brute-force attacks and credential stuffing bots.
🧠 Detection & MITRE ATT&CK Engine:
Auto-classifies events into MITRE ATT&CK techniques:
T1190: Exploit Public-Facing Application (SQLi)
T1083: File and Directory Discovery (Path Traversal / LFI)
T1059: Command and Scripting Interpreter (RCE)
T1552.001: Credentials In Files (Reconnaissance)
T1110.001: Password Guessing (Brute Force)
🌍 Threat Intelligence & Geolocation:
Enriches IP addresses with country, city, coordinates, ISP, and threat reputation scoring.
📊 Real-Time SOC Analyst Console (Streamlit):
Live incident stream with severity badges (Critical, High, Medium, Low).
Interactive Plotly world map showing geographic attack origins.
MITRE ATT&CK tactic/technique distribution charts.
Credential Harvester showing top targeted usernames and passwords.
Forensics search to investigate specific attacker IPs.
⚡ Automated Attack Simulator:
Built-in traffic generator with realistic SQLi, LFI, RCE, and brute-force payloads to test and demo the platform immediately.
📂 Project Structure
text

threat-sentinel/
├── config.py              # Ports, paths, and threat intel settings
├── main.py                # Master daemon starting decoy services
├── requirements.txt       # Dependencies (Streamlit, Plotly, Pandas, Requests)
├── core/
│   ├── db.py              # SQLite storage & fast analytics queries
│   ├── rules.py           # Signature & heuristic detection engine
│   └── enricher.py        # GeoIP & threat scoring engine
├── honeypot/
│   ├── http_honeypot.py   # Web decoy trapping web exploits & logins
│   └── ssh_honeypot.py    # SSH banner & credential decoy
├── dashboard/
│   └── app.py             # Streamlit SOC Analyst Console
└── simulator/
    └── attack_sim.py      # Automated attack traffic generator
🚀 Quickstart Guide
1. Install Dependencies
Open your terminal inside this directory and install the requirements:

bash

pip install -r requirements.txt
2. Start the Honeypot Services
In Terminal 1, launch the honeypot background services:

bash

python main.py
This starts the HTTP honeypot on http://localhost:8080 and the SSH decoy on port 2222.

3. Launch the SOC Analyst Dashboard
In Terminal 2, start the Streamlit web console:

bash

streamlit run dashboard/app.py
The dashboard will automatically open in your web browser at http://localhost:8501.

4. Fire Test Attacks (Live Demo Mode)
In Terminal 3, run the built-in attack simulator to generate live threat traffic:

bash

python simulator/attack_sim.py
Switch over to your browser dashboard to watch the attacks, world map, and MITRE metrics update in real time!

💼 Resume & Interview Talking Points
When presenting this project to recruiters and interviewers for SOC Analyst, Security Engineer, or Cybersecurity Consultant roles:

"Why did you build this?"

"I wanted hands-on experience with the complete threat detection lifecycle—from initial ingress and telemetry collection to log normalization, MITRE ATT&CK classification, and visual triage in a SIEM dashboard."

"How does the detection engine work?"

"Incoming HTTP and SSH connection data are parsed and evaluated against regular expression signatures and heuristic rules mapped directly to MITRE ATT&CK techniques like T1190 and T1110, assigning severity rankings from INFO to CRITICAL."

"How is data enriched?"

"Each attacker IP is correlated against an external GeoIP service and cached locally to prevent rate limiting. The engine assigns threat reputation scores based on attack aggressiveness and payload severity."
