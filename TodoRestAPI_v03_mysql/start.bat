@echo off
echo ===================================================
echo Starte Applikations-Infrastruktur...
echo ===================================================

:: 1. Auf Laufwerk E: wechseln und in den Projektordner gehen
E:
cd "E:\python_db_kurs\py_workspace\TodoRestAPI_v03_mysql"

:: 2. Pfad zum Python-Interpreter im Venv OHNE Anfuehrungszeichen definieren
set VENV_PYTHON=E:\python_db_kurs\py_workspace\TodoRestAPI_v03_mysql\venv\Scripts\python.exe

:: 3. Den Python-Pfad auf das aktuelle Verzeichnis setzen
set PYTHONPATH=%CD%

:: 4. FastAPI Backend im Hintergrund starten
echo [BACKEND] Starte FastAPI Backend...
start "FastAPI_Backend" /b "%VENV_PYTHON%" -m uvicorn main:app --host 127.0.0.1 --port 8000

:: 5. Kurz warten, bis das Backend bereit ist
timeout /t 3 /nobreak >nul

:: 6. Streamlit Frontend in einem separaten Fenster starten
echo [FRONTEND] Starte Streamlit Frontend...
start "Streamlit_Frontend" "%VENV_PYTHON%" -m streamlit run app.py --server.port 8501

echo ===================================================
echo Startbefehle wurden ausgefuehrt!
echo ===================================================
pause
