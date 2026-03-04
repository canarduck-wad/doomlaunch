# 🔴 DOOMLAUNCH

```
 ▄▖▄▖▖ ▖▖ ▄▖▖▖▖ ▖▄▖▖▖
 ▌▌▌▌▌▌▛▖▞▌▌ ▌▌▌▌▛▖▌▌
 ▙▌ ▙▘▙▌▙▌▌▝ ▌▙▖▛▌▙▌▌▝▌▙▖▌▌
```

> **Drag & Drop Doom Launcher for Linux Terminal** — Launch any `.pk3` or `.wad` file in one gesture.

---

## ✨ Features

- 🎨 **Animated rainbow ASCII banner** on launch
- 🖱️ **True drag & drop** — just drag your file into the terminal and hit Enter
- 🔍 **Auto-detects** GZDoom, ZDoom, LZDoom, Crispy-Doom, and PrBoom
- 🎮 **IWAD chooser** — pick Doom 1 or Doom 2 at launch, auto-located from common paths
- 📁 Supports `.pk3`, `.wad`, `.pk7`, `.ipk3`
- ✅ Confirmation prompt with full command preview before launch
- ⌨️ Works as a command-line argument or fully interactive

---

## 📋 Requirements

- **Python 3.6+** (pre-installed on most Linux distros)
- A **Doom engine**: [GZDoom](https://zdoom.org/downloads), ZDoom, LZDoom, Crispy-Doom, or PrBoom
- An **IWAD** file: `doom.wad` (Doom 1) and/or `doom2.wad` (Doom 2)

---

## 🚀 Installation

### Option 1 — Quick (run anywhere)

```bash
git clone https://github.com/yourname/doomlaunch.git
cd doomlaunch
chmod +x doomlaunch.py
./doomlaunch.py
```

### Option 2 — Global install (use from anywhere)

```bash
sudo cp doomlaunch.py /usr/local/bin/doomlaunch
sudo chmod +x /usr/local/bin/doomlaunch
```

Now you can type `doomlaunch` from any terminal.

---

## 🗂️ IWAD Setup

Place your official Doom WAD files in one of these auto-detected directories:

| Path | Notes |
|------|-------|
| `~/.local/share/doom/` | ✅ Recommended |
| `~/doom/` | Simple home folder |
| `/usr/share/games/doom/` | System-wide install |
| Current working directory | Fallback |

Supported IWAD filenames: `doom.wad`, `DOOM.WAD`, `doom1.wad`, `doom2.wad`, `DOOM2.WAD`

---

## 🎮 Usage

### Method 1 — Drag & Drop (the whole point!)

```bash
doomlaunch
```

Then **drag your `.pk3` or `.wad` file** from your file manager into the terminal window and press **Enter**.

### Method 2 — Direct argument

```bash
doomlaunch /path/to/mymod.pk3
doomlaunch ~/Downloads/brutal_doom.wad
```

### What happens next?

1. The animated banner plays 🎨
2. You choose **Doom 1** or **Doom 2** as your base game
3. A command summary is shown
4. Confirm → DOOM launches 🔥

---

## 🔍 Engine Auto-Detection Order

doomlaunch searches your `PATH` for these engines in order:

1. `gzdoom` ← preferred
2. `zdoom`
3. `lzdoom`
4. `crispy-doom`
5. `prboom-plus`
6. `prboom`

To install GZDoom on Ubuntu/Debian:

```bash
sudo apt install gzdoom
# or download from https://zdoom.org/downloads
```

---

## 📁 Project Structure

```
doomlaunch/
├── doomlaunch.py     # Main launcher script
└── README.md         # This file
```

---

## 🤝 Contributing

Pull requests are welcome! Ideas for improvement:

- Support for multiple PWAD files at once
- Config file for default engine/IWAD paths
- Flatpak / AppImage packaging
- Tab completion for shell integration

---

## 📜 License

MIT License — do whatever you want, just don't run with scissors.

---

## 🩸 Made with

- Python 3
- ANSI escape codes
- Terminal love
- And the eternal motivation of **RIPPING AND TEARING**
