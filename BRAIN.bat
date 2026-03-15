@echo off
cd %LOCALAPPDATA%\programs\Ollama
ollama.exe run llama3.2:1b
pause