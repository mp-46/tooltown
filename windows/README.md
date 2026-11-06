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

For a very simple, beginner-friendly guide, see **[HOW_TO_CREATE_INSTALLER.md](../HOW_TO_CREATE_INSTALLER.md)**.

### Quick 1-Click Rebuild
Inside `installer/`, simply double-click **`BUILD_INSTALLER.bat`**. It will automatically locate the compiler, build the installer, and open the `dist/` folder with your new `MysteryOfTooltown_Setup.exe`.

### How to Compile Locally in Inno Setup
1. Inno Setup 6 is installed on this PC (or downloadable from [jrsoftware.org](https://jrsoftware.org/isdl.php)).
2. Right-click `installer/tooltown_setup.iss` and select **Compile**.
3. The standalone installer `MysteryOfTooltown_Setup.exe` will be generated in `dist/`.

### Automated GitHub Builds
A GitHub Actions workflow (`.github/workflows/build-windows-installer.yml`) is included in this repository. It automatically builds the Windows installer executable on Windows Server runners upon release and provides downloadable artifacts.

---

## 🛠️ Architecture & Compatibility

* **Original Executable**: Macromedia Director 4 (`MV93`) 16-bit New Executable (`TOOL.EXE`).
* **Compatibility Layer**: OpenThunk VDM (WineVDM v0.9.0), translating 16-bit Windows API calls into 64-bit Windows 11 kernel calls.
* **Display Support**: Automatically runs in high-compatibility windowed mode with integer-friendly scaling.

