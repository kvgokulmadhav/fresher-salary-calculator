@echo off
TITLE Run Fresher ROI Calculator

echo ====================================================
echo Starting Fresher ROI & Minimum Salary Calculator...
echo ====================================================

:: Check if python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python is missing!
    echo Your computer does not have Python installed, or it is not added to the PATH.
    echo Streamlit applications require Python to run.
    echo.
    echo To fix this:
    echo 1. The Microsoft Store will now open automatically to install Python.
    echo 2. Click "Get" or "Install" in the Microsoft Store.
    echo 3. Once installed, run this script again.
    echo.
    pause
    start ms-windows-store://pdp/?productid=9PJPW5LDXLZ5
    exit /b
)

:: Install all required dependencies
echo Installing required dependencies (this may take a moment)...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt

:: Run the Streamlit Application
echo.
echo Launching the application in your browser...
python -m streamlit run app.py

pause
