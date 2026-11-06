# 🪟 The Mystery of Tooltown (1996) — Windows 10 / 11 Edition

This directory contains the authentic original 1996 CD-ROM release of **The Mystery of Tooltown** packaged with an integrated, zero-configuration 16-bit compatibility engine ([WineVDM / OTVDM](https://github.com/otya128/winevdm)).

It runs smoothly and natively on **64-bit Windows 10 and Windows 11 (x64 and ARM64)** without requiring a virtual machine or complex emulator configuration.

---

## 🚀 Quick Start (Portable — No Install Required)

1. Clone or download this repository.
2. Open the `windows/` folder.
3. Double-click either:
   * **`Play Mystery of Tooltown.vbs`** (Recommended — completely silent launch, no command prompt window).
   * **`Play Mystery of Tooltown.bat`** (Standard launcher).
4. The game opens directly on your Windows desktop with original digitized sound and 256-color artwork!

To read the original 1996 electronic illustrated manual, double-click **`Launch Manual.vbs`** or **`Launch Manual.bat`**.

---

## 📦 Building the Full Windows 11 Installer (`Setup.exe`)

We include a complete Inno Setup script that builds a standalone `MysteryOfTooltown_Setup.exe` installer with:
* Standard Windows 11 installation wizard
* Installs to `C:\Program Files (x86)\The Mystery of Tooltown`
* Creates Start Menu shortcuts
* Creates Desktop icon with the authentic 1996 `TOOL.ICO` icon
* Registers a clean uninstaller in Windows 11 **Settings > Installed Apps**

### How to Compile Locally
1. Download and install [Inno Setup 6](https://jrsoftware.org/isdl.php) (free & open source).
2. Right-click `installer/tooltown_setup.iss` and select **Compile**.
3. The standalone installer `MysteryOfTooltown_Setup.exe` will be generated in `dist/`.

### Automated GitHub Builds
A GitHub Actions workflow (`.github/workflows/build-windows-installer.yml`) is included in this repository. It automatically builds the Windows installer executable on Windows Server runners upon release and provides downloadable artifacts.

---

## 🛠️ Architecture & Compatibility

* **Original Executable**: Macromedia Director 4 (`MV93`) 16-bit New Executable (`TOOL.EXE`).
* **Compatibility Layer**: OpenThunk VDM (WineVDM v0.9.0), translating 16-bit Windows API calls into 64-bit Windows 11 kernel calls.
* **Display Support**: Automatically runs in high-compatibility windowed mode with integer-friendly scaling.
