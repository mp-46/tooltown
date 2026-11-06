@echo off
setlocal
cd /d "%~dp0"
title Tooltown Electronic Manual

if not exist "game\TTMANUAL.EXE" (
    echo Error: game\TTMANUAL.EXE not found!
    pause
    exit /b 1
)

start "" "otvdm\otvdmw.exe" "game\TTMANUAL.EXE"
exit /b 0

