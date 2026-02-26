@echo off
echo Checking if Python is installed...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b
)

echo Checking for requirements...
pip install -r requirements.txt

echo Starting Streamlit app...
streamlit run app.py

pause
