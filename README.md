 Alpha-Cybersecurity
Professional cybersecurity tools and AI systems built from the ground up.

ABOUT:
Alpha Cybersecurity is a cybersecurity consulting firm offering home and small business security audits, AI-powered threat anaylysis, and automated reporting. Every tool in this repository was built in-house using python and local AI models.
Founded by a cybersecurity consultant with hands-on experience auditing real networks, identifying vulnerabilities, and delivering actionable security reports to clients.

Tools Built-

Network Scanner:
Discovers every device connected to a local network. Identies unknown or unauthorizsed devices that represent potential security risks.

Port Scanner:
Scans any device for open ports and flags dangerous ones - including Telnet (port 23), SMB (port 445), and Remote Desktop(port 3389) - with plain-english explanations of each risk.

Password Auditor:
Analyses password strength against lenth, complexity, and a database of the most commnly compromised passwords. Provides specific improvement recommendations.

AI Security Agent:
A locally-run AI assistant powered by Ollama and llama3.2. Answers cybersecurity questions, assists with threat analysis, and operates entirely on-device with no data sent to external servers.

Voice AI Agent:
A voice-activated cybersecurity assistant. Speak question, receive a spoken answer. Built with pyttsx3 and SpeechRecogniton, powered by the local AI model.

Automated Audit Report Generator:
Generates a branded, professional PDF security score, itemised vulnerabilities and prioritised recommendations. Delivered to clients after every audit.


Tech Stack-
Tool                                     Purpose
Python 3.12                           Core programming language
Ollama + llama3.2:1b                  Local AI model - runs on-device
fpdfx3                                PDF report generation
pyttsx3                               Text-to-speech for voice agent
SpeechRecognition                     Voice input processing
socket / subprocess                   Network scanning and port detection
PyTorch                               AI model experimentation and training

Services-

Home Security Audit:
A thorough audit of your home network and devices. Includes a written PDF report with every vulnerability found step-by-step fixes.
What we check:
-Router security setting and firmware
-WiFi encryption standard(WPA2/WPA3)
-All connected devices and unknown access
-Open ports on network devices
-Password strength across all accounts
-Phishing awareness and device update status

Deliverable:Professional PDF report within 24 hours.

Monthly Monitoring:
Remote monthly check of your network security status. Receive an update report each month showning your current security score and any new risks detected.

Small Business Audit:
Comprehensive security assessment for small businesses. Covers internal network, employee devices, remote access policies, and data protection practices.


Case Studies:

Audit 001-
Client: Residential household
Findings: Default router password in use, WPS enabled, 2 unrecoginised devices on network, 3 weak passwords idenified.
Resolution: All vulnerabilities remediated within the same session.
Security score improved from 40/100 to 95/100.

Audit 002-
Client: Residential household
Findings: WiFi using outdated WPA encryption, no guest network router admin panel exposed on open port.
Resolution: Encryption upgraded, guest network configured, admin access restricted. Full report delivered in 24 hours.

Audit 003-
Client: Residential household
Findings: 4 critical password vulnerabilities, smart TV on main network, outdated router firmware.
Resolution: Password manager deployed, IoT devices moved to guest network, firmware updated.


Certifications in progress:

-CompTIA security +-studying, exam schedule Month 6
-CEH(Certified Ethical Hacker):Study begins Month 6
-OSCP(Offensive Security):planned for College Year 2
-CISSP:College Year 3

Roadmap:
-Home network scanner
-Port scanner with risk flags
-Password strength auditor
-Local AI security agent
-Voice AI assistant
-Automated PDF audit report generator
-Web vulnerability scanner
-Phishing email detector
-AI fine-tuned on cybersecurity data(TinyLlama+MLX)
-Client web portal with dashboard
-Subscription app with proprietary AI model

Get In Touch
Intrested in a security audit for your home or business?
-GitHub: github.com/AlphaCyberSecurity
-Email: ishaan_gaur@hotmail.com
All audits are conducted with full written permission from the client. Alpha Cybersecurity operates in compliance with applicabble computer misuse and data protection laws.

Built with Python. Powered by local AI. Founded pre-college.
