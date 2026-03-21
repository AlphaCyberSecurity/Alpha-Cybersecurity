import time
import ollama
import pyttsx3
import os
import random
import threading
from watchdog.observers import Observer
from watchdog.event import FileSystemEventHandler

#VOICE ENGINE
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 0.9)

#Try to set a deeper voice if available
voice = engine.getProperty("voice")
for voice in voices:
    if "male" in voice.name.lower() or "david" in voice.name.lower() or "mark" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break

def speak(text):
    print(f"[SENTINEL]: {text}")
    engine.say(text)
    engine.runAndWait()

#STARTUP LINES
STARTUP_LINES = [
    "Initialising Alpha Cybersecurity Sentinel.",
    "Running system diagnostics.",
    "Voice engine online.",
    "AI brain connected.",
    "Threat detection algorithms loaded.",
    "Watching for incoming files.",
    "Alpha Cybersecurity Sentinel is fully operational. The firm is protected.",
]

#PATROL PHASES
PATROL_PHASES = [
    "All clear. No threats detected.",
    "Perimeter secure. Monitoring active.",
    "System nominal. Watching for anomalies.",
    "No suspicious activity. Standing by.",
    "Network quiet. Threat level low.",
    "Continous monitoring active. Nothing to report.",
    "Alpha Cybersecurity Sentinel online. Awaiting activity.",
    "All systems green. Ready to analyse.",
    "Surveillance active. Drop a file to test.",
]

#THREAT REACTIONS
def get_initial_reaction(filename):
    name_lower = filename.lower()
    if any(w in name_lower for w in ["virus", "malware", "hack", "trojan", "ransomeware", "worm"]):
        return random.choice([
            "Warning! Highly suspicious filename detected. Analysing immediately.",
            "Alert. This file name contains know threat indicators. Engaging AI brain.",
            "Threat flag raised. Running full analysing now.",
        ])
    elif any(w in name_lower for w in ["exe", "bat", "cmd", "ps1", "vbs", "scr"]):
        return random.choice([
            "Caution! Executable file type detected. This could be dangerous.",
            "Executable detected. These file types are commnly used in attacks.",
            "Warning. This file types can run code on your system. Analysing.",
        ])
    elif any(w in name_lower for w in ["invoice", "urgent", "payment", "bank", "account"]):
        return random.choice([
            "Social engineering pattern detected. This looks like a phishing attempt.",
            "Warning! This filename matches common phishing document patterns.",
            "Caution! Financial lure detected. Could be a scam document.",
        ])
    elif any(w in name_lower for w in ["free", "crack", "keygen", "patch", "serial"]):
        return random.choice([
            "Piracy related filename detected. These files often contain hidden malware.",
            "Warning. Software crack filename are a major malware delivery method.",
            "Suspicious. Free software cracks frequently bundle ransomware.",
        ])
    else:
        return random.choice([
            "New file detected. Initiating threat analysis."
            "File incoming. Scanning with AI brain.",
            "Item detected. Checking threat level now.",
        ])

#AI BRAIN
def analyse_file(filename):
    try:
        prompt = (
            "You are SENTINEL, an AI security system for Alpha Cybersecurity. "
            "A file called '" + filename + "' just appeared in monitored folder. "
            "Respond with exactly three short sentences. "
            "Sentence one: give a risk score from 1 to 10 and say Safe, Suspicious, or Dangerous. "
            "Sentence two: explain the main reason for your assessment. "
            "Sentnece three: give one specific action the operator should take. "
            "Be confident, direct, and specific."
        )
        responce = ollama.generate(model='llama3.2:1b', prompt=prompt)
        return response['response']
    except Exception:
        return "AI brain connection lost. Please ensure Ollama is running."
    
def get_ai_security_tip():
    try: 
        tips = [
        "Give one suprising cybersecurity fact most people do not know. One sentence only.",
        "Give one quickly tip to improve home network security. One sentence only.",
        "Name one common way hacker get into home networks. One sentence only.",
        "Give one thing everyone should do to protect their passwords. one sentence only.",
        "What is one sign a computer might be infected with malware. One sentence only.",
        ]
        response = ollama.generate(
             model='llama3.2:1b',
             prompt=random.choice(tips)
        )
        return response['response']
    except Exception:
        return None
#FILE WATCHER
class SentinelHandler(FileEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            reaction = get_inital_reaction(filename)
            speak(reaction)
            speak("Filename:" + filename)
            speak("Engaging AI brain. Stand by.")
            result = analyse_file(filename)
            speak(result)
            print("\n" + "=" * 50)
            print("FILE:     " + filename)
            print("ANALYSIS: " + result)
            print("=" * 50 + "\n")

#PATROL LOOP
def patrol_loop():
    time.sleep(120)
    while True:
        time.sleep(random.randint(180, 300))
        if random.random() < 0.7:
            speak(random.choice(PATROL_PHRASES))
        else:
            speak("Accessing AI brain for security intelligence.")
            tip = get_ai_security_tip()
            if tip:
                speak("Security tip. " + tip)

#STARTUP
WATCH_FOLDER = r"C:\Users\Ishaa\OneDrive\Dekstop\Alpha-cybersecurity\SHIELD_FOLDER"

if not os.path.exists(WATCH_FOLDER):
    os.makedirs(WATCH_FOLDER)

for line in STARTUP_LINES:
    speak(line)
    time.sleep(0.3)

print("\n[SENTINEL]: Drop any file into SHIELD_FOLDER to test.")
print("\n[SENTINEL]: Press Ctrl+C to shut down.\n")

patrol_thread = threading.Thread(target=patrol_loop, daemon=True)
patrol_thread.start()

observer = Observer()
observer.schedule(SentinelHandler(), WATCH_FOLDER, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
    speak("Sentinel shutting down. Alpha Cybersecurity signing oof. Stay Secure.")
    print("[SENTINEL]: Offline.")