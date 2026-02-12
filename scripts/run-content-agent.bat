@echo off
echo ==========================================
echo Rising Sun Digital - Content Agent
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Navigate to scripts directory
cd /d "%~dp0"

REM Run the content agent
echo Running content agent...
echo.

if "%1"=="--generate" (
    python content-agent.py --generate
) else if "%1"=="--sample" (
    python content-agent.py --sample
) else (
    python content-agent.py %*
)

echo.
pause
