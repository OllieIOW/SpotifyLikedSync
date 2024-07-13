@echo off
set LOG_DIR=%~dp0\logs
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set LOG_FILE=%LOG_DIR%\sync_log.txt
if exist "%LOG_FILE%" del "%LOG_FILE%"
python "%~dp0\sync.py" >> "%LOG_FILE%" 2>&1