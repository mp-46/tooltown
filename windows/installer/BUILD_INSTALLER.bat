@echo off
setlocal
cd /d "%~dp0"
title Mystery of Tooltown - Installer Builder

echo ========================================================
echo   The Mystery of Tooltown - Building Windows 11 Installer
echo ========================================================
echo.

set "ISCC_PATH="

:: Check common Inno Setup 6 installation paths
if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Inno Setup 6\ISCC.exe" (
    set "ISCC_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Inno Setup 6\ISCC.exe"
) else if exist "%LOCALAPPDATA%\Programs\Inno Setup 6\ISCC.exe" (
    set "ISCC_PATH=%LOCALAPPDATA%\Programs\Inno Setup 6\ISCC.exe"
) else if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    set "ISCC_PATH=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
) else if exist "C:\Program Files\Inno Setup 6\ISCC.exe" (
    set "ISCC_PATH=C:\Program Files\Inno Setup 6\ISCC.exe"
)

if "%ISCC_PATH%"=="" (
    echo [!] Inno Setup 6 was not found on your system.
    echo.
    echo Would you like to install it automatically using Windows Package Manager (winget)?
    echo Press any key to install Inno Setup, or close this window to cancel.
    pause >nul
    winget install JRSoftware.InnoSetup --accept-source-agreements --accept-package-agreements --silent
    if exist "%LOCALAPPDATA%\Programs\Inno Setup 6\ISCC.exe" (
        set "ISCC_PATH=%LOCALAPPDATA%\Programs\Inno Setup 6\ISCC.exe"
    ) else if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
        set "ISCC_PATH=C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
    )
)

if "%ISCC_PATH%"=="" (
    echo [X] Could not locate ISCC.exe compiler.
    echo Please download and install Inno Setup 6 from: https://jrsoftware.org/isdl.php
    pause
    exit /b 1
)

echo [*] Compiling installer with: "%ISCC_PATH%"
echo [*] Script: tooltown_setup.iss
echo.

"%ISCC_PATH%" "tooltown_setup.iss"

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo   SUCCESS! Installer created at:
    echo   ..\..\dist\MysteryOfTooltown_Setup.exe
    echo ========================================================
    echo.
    echo Opening output folder...
    start "" explorer.exe "%~dp0..\..\dist"
) else (
    echo.
    echo [X] An error occurred during compilation.
)

pause
