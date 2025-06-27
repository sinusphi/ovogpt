@echo off

REM check if server is running and if yes kill it
for /f "tokens=2 delims=," %%a in ('tasklist /FI "IMAGENAME eq python.exe" /FO CSV /NH') do (
    for /f "delims=" %%b in ('wmic process where "ProcessId=%%a and CommandLine like '%%ovo.py%%'" get ProcessId /value 2^>nul') do (
        set "line=%%b"
        for /f "tokens=2 delims==" %%c in ("%%b") do (
            taskkill /PID %%c /F >nul
        )
    )
)

REM check if venv exists
if not exist ".venvs\ovo-venv\Scripts\activate.bat" (
    echo [ERROR] No virtual environment found!
    echo Please run setup.bat first.
    pause
    exit /b
)

REM activate venv
call .venvs\ovo-venv\Scripts\activate.bat

REM start server
python ovogpt\ovo.py

REM deactivate venv
deactivate

pause