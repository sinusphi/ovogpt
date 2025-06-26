@echo off
REM check if server is running and if so kill
for /f "tokens=2 delims=," %%a in ('tasklist /FI "IMAGENAME eq python.exe" /FO CSV /NH') do (
    for /f "delims=" %%b in ('wmic process where "ProcessId=%%a and CommandLine like '%%ovo.py%%'" get ProcessId /value 2^>nul') do (
        set "line=%%b"
        for /f "tokens=2 delims==" %%c in ("%%b") do (
            taskkill /PID %%c /F >nul
        )
    )
)

REM activate venv and start server
call .venvs\ovo-venv\Scripts\activate.bat
python ovogpt\ovo.py

REM deactivate venv
deactivate

pause