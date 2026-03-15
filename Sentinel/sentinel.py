import time
import ollama
import pyttsx3
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


engine = pyttsx3.init()
def speak(text)
print(f"[SENTINEL VOICE]: {text}")
engine.say(text)
engine.runAndWait()



class SentinelHandler(FileSystemEventHandler):
def on_created(self, event):
if not event.is_directory:
filename = os.path.basename(event.src_path)
speak(f"Alert. New file detected: {filename}")

try:
prompt = f"Analyze this filename for security risk: '{filename}'. Is it malware or phishing? Give a RISK SCORE 1-10."
response = ollama.generate(model='llama.3.2:1b', prompt=prompt)
except Exception as e:
speak("Brain connection error. Please ensure Ollama is running.")




path_to_watch = "C:\\Sentinel_Shield"
if not os.path.exists(path_to_watch): os.markedirs(oath_to_watch)
speak("Sentinel System is online. Protecting the firm.")
observer = Observer()
observer.schedule(SentinelHandler(), path_to_watch, recursive=False)
observer.start()

try:
while True: time.sleep(1)
except KeyboardInterrupt:
observer.stop()