import time
import ollama
import pyttsx3
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Voice Engine
engine = pyttsx3.init()
engine.setProperty("rate", 155)
engine.setProperty("volume", 0.9)

def speak(text):
    print(f"[SENTINEL]: {text}")
    engine.say(text)
    engine.runAndWait()

#AI Brain
def analyse_file(filename):
    try:
        prompt = (
            f"Complete this security log entry: File detected: '{filename}'. THREAT LEVEL: [1-10]. This file is [Safe/Suspicious/Dangerous] because [one reason]. Assessment:"
        )
        response = ollama.generate(model='llama3.2:1b', prompt=prompt)
        return response['response']
    except Exception:
        return "Brain offline. Please esure Ollama is running."
    
#File Watcher
class SentinelHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            speak(f"Alert! New file detected: {filename}")
            speak(f"Analysing threat level. Stand By.")
            result = analyse_file(filename)
            speak(f"Analysis complete. {result}")
            print(f"\n[FULL REPORT]\nFile: {filename}\n{result}\n")
    
#Startup
WATCH_FOLDER = r"C:\Users\Ishaa\OneDrive\Desktop\Alpha-Cybersecurity\SHIELD_FOLDER"

if not os.path.exists(WATCH_FOLDER):
    os.makedirs(WATCH_FOLDER)
    print(f"[SENTINEL]: Created watch folder at {WATCH_FOLDER}")

speak("Alpha Cybersecurity Sentinel is online. The firm is protected.")
print(f"Drop any file into SHIELD_FOLDER to test it.")
print(f"[SENTINEL]: Press Ctrl+C to shut down. \n")

observer = Observer()
observer.schedule(SentinelHandler(), WATCH_FOLDER, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
    speak("Sentinel shutting down. Stay secure.")
    print("[SENTINEL]: Offline.")