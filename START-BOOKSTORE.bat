@echo off

rem Get the file path of batch file
set "script_dir=%~dp0"

rem Run Python script(which is inside myBookstore folder)
python "%script_dir%\myBookstore\book_store.py"
pause
