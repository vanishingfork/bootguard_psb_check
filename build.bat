@echo off
setlocal enabledelayedexpansion

REM Check Python installation
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python not found. Please install Python 3.x
    exit /b 1
)

REM Check if RW.exe exists in current directory
if not exist RW.exe (
    echo RW.exe not found in current directory
    exit /b 1
)

REM Create virtual environment if not exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment and install requirements
call venv\Scripts\activate.bat
python -m pip install pyinstaller

REM Build the executable
python -m PyInstaller --onefile firmware_integrity.py ^
    --add-binary "%CD%\RW.exe;." ^
    --uac-admin ^
    --workpath build ^
    --specpath build ^
    --distpath dist

REM Clean up
if exist build rmdir /s /q build
if exist firmware_integrity.spec del /f /q firmware_integrity.spec

REM Deactivate virtual environment
deactivate

echo Build complete! Executable is in the dist folder
pause