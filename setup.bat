@echo off

REM create venv if not exists
if not exist ".venvs\ovo-venv" (
    python -m venv .venvs\ovo-venv
)

REM activate venv
call .venvs\ovo-venv\Scripts\activate.bat

REM install requirements
python -m pip install -U pip
pip install -r requirements.txt

REM deactivate venv
deactivate

REM 
echo Installation complete! Run start_server.bat to open the chat page. 

pause