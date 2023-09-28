@echo off

rem Check if pip is installed
where pip >nul 2>nul
if errorlevel 1 (
    echo Pip is not installed. Installing pip...
    rem Robust approach when install pip automatically
    python -m ensurepip --default-pip
    rem Handle the unlikely event that the Batch file fails.
    if errorlevel 1 (
        echo Failed to install pip. Please install it manually.
        pause
        exit /b 1
    ) else (
        echo Pip has been successfully installed.
    )
) else (
    echo Pip is already installed.
)

rem Get the file path of batch file
set "script_dir=%~dp0"

rem Run Python script(which is inside myBookstore folder)
python "%script_dir%\myBookstore\book_store.py"
pause
