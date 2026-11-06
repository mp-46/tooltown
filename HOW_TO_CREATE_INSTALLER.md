# 📦 How to Build & Use the Windows 11 Installer

This guide explains in very simple terms what the installer is, where to find it, and how to create it yourself.

---

## 💡 What Is `MysteryOfTooltown_Setup.exe`?

It is a single file (like any game installer you download from Steam or GOG). 

When you (or anyone you send it to) double-clicks `MysteryOfTooltown_Setup.exe`:
1. A standard Windows Installation Wizard appears.
2. It installs the game to `C:\Program Files (x86)\The Mystery of Tooltown`.
3. It puts a **Mystery of Tooltown** shortcut on your **Desktop** and in your **Start Menu** with the original 1996 Tooltown icon.
4. When finished, it gives you a checkbox to launch the game immediately.
5. It registers in Windows 11 **Settings > Apps > Installed apps**, so it can be cleanly uninstalled anytime.

---

## ✨ Option 1: It Is Already Built! (Ready Right Now)

Your installer has already been compiled on this machine and is waiting for you:

📁 **Location:**
`tooltown\dist\MysteryOfTooltown_Setup.exe`

You can take that 5 MB file, copy it to a USB flash drive, email it, or put it on any Windows 10 or Windows 11 PC, double-click it, and play!

---

## 🔨 Option 2: How to Re-Build It with 1 Click

If you ever change files or want to rebuild the installer from scratch:

1. Open the folder:
   [`tooltown\windows\installer\`](windows/installer/)
2. Double-click the file named:
   **`BUILD_INSTALLER.bat`**
3. A small command window will appear and compile the installer in about 10 seconds.
4. When finished, it will automatically open the `dist` folder showing your brand new **`MysteryOfTooltown_Setup.exe`**!

---

## 🖥️ Option 3: Using the Inno Setup Visual Program

If you prefer using the graphical visual editor:

1. [Inno Setup 6](https://jrsoftware.org/isdl.php) is already installed on this machine.
2. Go to [`tooltown\windows\installer\`](windows/installer/).
3. **Right-click** on `tooltown_setup.iss`.
4. Choose **Compile** (or open it and press **F9** / click the green **Play** button at the top).
5. The bottom log will scroll and say `Successful compile`.
6. Your installer will be in `tooltown\dist\MysteryOfTooltown_Setup.exe`.

---

## 🌐 Option 4: Download via GitHub (No tools needed)

If you are on a different computer and don't want to install any developer tools:
1. Go to your GitHub repository: [github.com/mp-46/tooltown](https://github.com/mp-46/tooltown)
2. Click the **Actions** tab at the top.
3. Click the latest **Build Windows 11 Installer** run.
4. Under **Artifacts**, click **`MysteryOfTooltown_Setup`** to download the ready-to-run installer zip!

