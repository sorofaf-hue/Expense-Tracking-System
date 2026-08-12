@echo off

cd /d "%~dp0"

start /min "Backend" cmd /c "cd backend && uvicorn server:app --reload"

timeout /t 3 /nobreak >nul

start /min "Frontend" cmd /c "streamlit run frontend/app.py"

exit