@echo off
echo ==========================================
echo   OrangeHRM Automation Test Execution
echo ==========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo Starting test execution...
echo.

REM Run tests
pytest tests\test_orangehrm_workflow.py -v --html=reports\report.html --self-contained-html

echo.
echo ==========================================
echo   Test Execution Completed!
echo ==========================================
echo.
echo View HTML Report: reports\report.html
echo Check Logs: reports\logs\
echo Screenshots: reports\screenshots\
echo.
pause
