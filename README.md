# ⚙️ The Mystery of Tooltown (1996) — Remaster

> **An authentic HTML5 & Touchscreen remaster of the 1996 CD-ROM edutainment classic *The Mystery of Tooltown*, restored with original 256-color VGA art and digitized audio.**

[![Live Demo](https://img.shields.io/badge/Demo-Play%20Online-brightgreen?style=for-the-badge&logo=googlechrome)](https://mp-46.github.io/tooltown/)
[![Platform](https://img.shields.io/badge/Platform-HTML5%20%7C%20Touch%20%7C%20Desktop-blue?style=for-the-badge)](https://github.com/mp-46/tooltown)
[![Original](https://img.shields.io/badge/Original-1996%20Macromedia%20Director%204-orange?style=for-the-badge)](https://archive.org/details/the-mystery-of-tooltown)

---

## 📖 Story & Premise

Something strange is happening in **Tooltown**! Deep in the **Valley of the Machines**, the great mechanical generators and turbines that power the entire city have ground to a halt. The Mayor has called upon **Detective Oslo** and the Geological Society to investigate.

Travel across the Valley, collect authentic simple machines in your backpack, learn classical mechanical advantage principles (levers, pulleys, inclined planes, screws, wedges, wheel & axles), solve the gear train mechanisms, and restore power to Tooltown!

---

## 🎮 Controls

The game has been modernized for **mobile phones, iPads, tablets, and desktop computers**:

* 📱 **Touchscreen:** Tap hotspots, character dialogue, items, and map pins directly.
* 🖱️ **Mouse:** Point-and-click interface with hovering tooltip discovery.
* ⌨️ **Keyboard Shortcuts:**
  * **`M` / `Tab`**: Open / Toggle Valley of the Machines Map
  * **`B` / `I`**: Open Oslo's Backpack & Simple Machine Journal
  * **`1` – `6`**: Quick-select inventory tool slots
  * **`R`**: Reset current room / mechanism
  * **`Esc`**: Exit to Title Screen

---

## 🎨 Authentic 1996 Restoration

Unlike AI-generated reimaginings or generic vectors, this version utilizes **100% authentic 1996 assets** reverse-engineered and extracted directly from the original Redump CD-ROM Macromedia Director 4 (`MV93`) `.DIR` binaries:

* **Authentic 256-Color VGA Hand-Painted Backgrounds:**
  * Title Splash Screen (`tool_splash.png`)
  * Valley of the Machines Panoramic Map
  * Oslo's Inventor House & Workshop
  * Higgins' Grocery Store & Grain Mill
  * Machine Mall / Al's Repair Shop
  * University Science Hall
  * Museum of Ancient Antiquities
  * Subterranean Ancient Machine Core
* **Original Detective Oslo Sprites & Portraits:**
  * Detective Oslo/Rick 1996 pixel-art character portraits.
  * Grocer Higgins, Curator Archimedes, and Professor Gearson.
* **Hand-Drawn Simple Machine Toolset:**
  * Authentic forged crowbar, block & tackle pulley, hand drill, pointy shovel, and map fragment.
* **Digitized 1996 Sound Effects:**
  * Original Foley sound effects: creaking doors, spinning bicycle wheels, discovery chimes, and interface clicks.

---

## 🎓 Simple Machine Educational Mechanics

The game explores the physics of all **6 classical simple machines**:

1. **Class 1 Lever (Crowbar):** Converts a small downward force at a long distance into massive upward prying force at the fulcrum.
2. **Compound Pulley (Block & Tackle):** Divides load weight across supporting rope strands to hoist heavy machinery.
3. **Wheel & Axle (Gears & Winch):** Modifies torque and speed ratios between drive wheels and driven axles.
4. **Inclined Plane (Ramp):** Reduces required lifting force by increasing travel distance.
5. **Screw Mechanism (Hand Drill / Jackscrew):** Rotates an inclined plane wrapped around a cylinder to produce high linear thrust.
6. **Double Inclined Plane (Wedge / Shovel):** Directs driving force outward to split and separate heavy obstacles.

---

## 🚀 Running Locally

Clone this repository and serve it with any local HTTP server:

```bash
git clone https://github.com/mp-46/tooltown.git
cd tooltown
python -m http.server 8080
```

Then open `http://localhost:8080` in any web browser!

---

## 📜 Credits & Provenance

* **Original Game:** *The Mystery of Tooltown* (1996, Tooltown Inc. / Mac & Windows CD-ROM).
* **Extraction Tooling:** Custom Python RIFX/PackBits unpacker leveraging ScummVM Director reverse-engineering research.

