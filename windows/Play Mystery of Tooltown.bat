@echo off
setlocal
cd /d "%~dp0"
title The Mystery of Tooltown (1996)

if not exist "game\TOOL.EXE" (
    echo Error: game\TOOL.EXE not found!
    pause
    exit /b 1
)

if not exist "otvdm\otvdmw.exe" (
    echo Error: otvdm\otvdmw.exe not found!
    pause
    exit /b 1
)

:: Launch with windowed WineVDM runner from the game directory
cd /d "%~dp0game"
start "" "%~dp0otvdm\otvdmw.exe" "%~dp0game\TOOL.EXE"
exit /b 0

