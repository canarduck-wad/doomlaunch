#!/usr/bin/env python3
"""
doomlaunch - Drag & Drop Doom launcher for Linux terminal
Usage: doomlaunch [file.pk3 | file.wad]
       Or just run and drag & drop the file into the terminal!
"""

import sys
import os
import subprocess
import time
import threading
import itertools

# ─── ANSI Colors ────────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
COLORS  = [
    "\033[91m",  # bright red
    "\033[93m",  # bright yellow
    "\033[92m",  # bright green
    "\033[96m",  # bright cyan
    "\033[94m",  # bright blue
    "\033[95m",  # bright magenta
    "\033[31m",  # red
    "\033[33m",  # yellow
]

DOOM_RED    = "\033[91m"
DOOM_YELLOW = "\033[93m"
DOOM_GRAY   = "\033[90m"
WHITE       = "\033[97m"

# ─── ASCII Art ───────────────────────────────────────────────────────────────
ASCII_LINES = [
    " ▄▖▄▖▖ ▖▖ ▄▖▖▖▖ ▖▄▖▖▖",
    " ▌▌▌▌▌▌▛▖▞▌▌ ▌▌▌▌▛▖▌▌",
    " ▙▌ ▙▘▙▌▙▌▌▝ ▌▙▖▛▌▙▌▌▝▌▙▖▌▌",
]

SEPARATOR = "─" * 50

# ─── Animated ASCII Banner ───────────────────────────────────────────────────
stop_animation = threading.Event()

def animate_banner():
    color_cycle = itertools.cycle(COLORS)
    frame = 0
    while not stop_animation.is_set():
        lines_colored = []
        for i, line in enumerate(ASCII_LINES):
            # Each character gets a shifting color for rainbow effect
            colored_line = ""
            for j, ch in enumerate(line):
                color_idx = (frame + i * 5 + j * 2) % len(COLORS)
                colored_line += COLORS[color_idx] + ch
            colored_line += RESET
            lines_colored.append(colored_line)

        # Move cursor up to overwrite previous frame (after first frame)
        if frame > 0:
            sys.stdout.write(f"\033[{len(ASCII_LINES) + 4}A")

        # Print frame
        print()
        print(f"  {DOOM_RED}{BOLD}{SEPARATOR}{RESET}")
        for line in lines_colored:
            print(f"  {line}")
        print(f"  {DOOM_RED}{BOLD}{SEPARATOR}{RESET}")
        print()
        sys.stdout.flush()

        frame += 1
        time.sleep(0.08)

def print_banner_static():
    """Print banner once with rainbow colors (no animation)."""
    print()
    print(f"  {DOOM_RED}{BOLD}{SEPARATOR}{RESET}")
    for i, line in enumerate(ASCII_LINES):
        colored_line = ""
        for j, ch in enumerate(line):
            color_idx = (i * 7 + j * 3) % len(COLORS)
            colored_line += COLORS[color_idx] + ch
        colored_line += RESET
        print(f"  {colored_line}")
    print(f"  {DOOM_RED}{BOLD}{SEPARATOR}{RESET}")
    print()

def start_animation():
    t = threading.Thread(target=animate_banner, daemon=True)
    t.start()
    return t

def stop_anim(t):
    stop_animation.set()
    t.join(timeout=1)
    # Clear animation area and reprint static
    sys.stdout.write(f"\033[{len(ASCII_LINES) + 4}A")
    sys.stdout.write("\033[J")  # Clear from cursor to end
    print_banner_static()

# ─── Find IWAD ───────────────────────────────────────────────────────────────
COMMON_PATHS = [
    os.path.expanduser("~/.local/share/doom"),
    os.path.expanduser("~/doom"),
    "/usr/share/games/doom",
    "/usr/share/doom",
    "/opt/doom",
    os.getcwd(),
]

DOOM1_NAMES = ["doom.wad", "DOOM.WAD", "doom1.wad", "DOOM1.WAD"]
DOOM2_NAMES = ["doom2.wad", "DOOM2.WAD"]

def find_wad(names):
    for directory in COMMON_PATHS:
        for name in names:
            path = os.path.join(directory, name)
            if os.path.isfile(path):
                return path
    return None

def find_engine():
    for engine in ["gzdoom", "zdoom", "lzdoom", "crispy-doom", "prboom-plus", "prboom"]:
        result = subprocess.run(["which", engine], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    return None

# ─── UI Helpers ──────────────────────────────────────────────────────────────
def color_input(prompt):
    return input(f"  {DOOM_YELLOW}{BOLD}{prompt}{RESET} ")

def info(msg):
    print(f"  {DOOM_GRAY}▸{RESET} {msg}")

def success(msg):
    print(f"  {DOOM_RED}{BOLD}▸{RESET} {WHITE}{msg}{RESET}")

def error(msg):
    print(f"  {DOOM_RED}{BOLD}[ERREUR]{RESET} {msg}")

def warn(msg):
    print(f"  {DOOM_YELLOW}{BOLD}[!]{RESET} {msg}")

# ─── Main Logic ───────────────────────────────────────────────────────────────
def choose_iwad():
    doom1 = find_wad(DOOM1_NAMES)
    doom2 = find_wad(DOOM2_NAMES)

    print(f"  {DOOM_YELLOW}{BOLD}choose your IWAD:{RESET}")
    print()

    options = []
    if doom1:
        print(f"  {DOOM_RED}[1]{RESET} {WHITE}DOOM 1{RESET}  {DOOM_GRAY}({doom1}){RESET}")
        options.append(("doom1", doom1))
    else:
        print(f"  {DOOM_GRAY}[1] DOOM 1  (not found){RESET}")

    if doom2:
        print(f"  {DOOM_RED}[2]{RESET} {WHITE}DOOM 2{RESET}  {DOOM_GRAY}({doom2}){RESET}")
        options.append(("doom2", doom2))
    else:
        print(f"  {DOOM_GRAY}[2] DOOM 2  (not found){RESET}")

    print(f"  {DOOM_RED}[3]{RESET} {WHITE}custom path{RESET}")
    print()

    while True:
        choice = color_input("your choice [1/2/3] →").strip()

        if choice == "1":
            if doom1:
                return doom1
            else:
                error("doom.wad not found. Place it in ~/.local/share/doom/ or ~/doom/")
        elif choice == "2":
            if doom2:
                return doom2
            else:
                error("doom2.wad not found. Place it in ~/.local/share/doom/ or ~/doom/")
        elif choice == "3":
            path = color_input("path to the IWAD →").strip().strip("'\"")
            if os.path.isfile(path):
                return path
            else:
                error(f"File not found: {path}")
        else:
            warn("enter 1, 2 or 3.")

def launch_doom(pwad_path, iwad_path, engine):
    pwad_path = os.path.abspath(pwad_path)
    
    cmd = [engine, "-iwad", iwad_path, "-file", pwad_path]
    
    print()
    print(f"  {DOOM_RED}{BOLD}{SEPARATOR}{RESET}")
    success(f"ENGINE : {os.path.basename(engine)}")
    success(f"IWAD   : {os.path.basename(iwad_path)}")
    success(f"PWAD   : {os.path.basename(pwad_path)}")
    print(f"  {DOOM_RED}{BOLD}{SEPARATOR}{RESET}")
    print()
    info(f"Commande: {' '.join(cmd)}")
    print()

    confirm = color_input("Lancer Doom ? [O/n] →").strip().lower()
    if confirm in ("", "o", "oui", "y", "yes"):
        print()
        success(">>> RIPPING AND TEARING... <<<")
        print()
        try:
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print()
            info("Closed launcher.")
    else:
        info("canceled.")

def get_file_interactive():
    print(f"  {DOOM_YELLOW}{BOLD}Drag and drop your .pk3 or .wad file here,{RESET}")
    print(f"  {DOOM_YELLOW}then press ENTER:{RESET}")
    print()
    path = color_input("→").strip()
    # Strip quotes added by some terminals on drag & drop
    path = path.strip("'\"")
    return path

def main():
    # ── Banner animation ──
    anim_thread = start_animation()
    time.sleep(1.8)  # Let it animate for a moment
    stop_anim(anim_thread)

    print(f"  {WHITE}{BOLD}DOOM LAUNCHER — Drag & Drop Edition{RESET}")
    print(f"  {DOOM_GRAY}for Linux Terminal{RESET}")
    print()

    # ── Get PWAD path ──
    if len(sys.argv) >= 2:
        pwad_path = sys.argv[1].strip().strip("'\"")
        info(f"File received: {DOOM_YELLOW}{pwad_path}{RESET}")
    else:
        pwad_path = get_file_interactive()

    # ── Validate file ──
    if not pwad_path:
        error("No file specified.")
        sys.exit(1)

    if not os.path.isfile(pwad_path):
        error(f"folder not found: {pwad_path}")
        sys.exit(1)

    ext = os.path.splitext(pwad_path)[1].lower()
    if ext not in (".pk3", ".wad", ".pk7", ".ipk3"):
        warn(f"Unusual extension: {ext}  (We'll continue anyway...)")

    print()

    # ── Find engine ──
    engine = find_engine()
    if not engine:
        error("No Doom engine found (gzdoom, zdoom, lzdoom, crispy-doom, prboom-plus).")
        print()
        info("Install GZDoom: https://zdoom.org/downloads")
        sys.exit(1)

    info(f"Motor detected: {DOOM_YELLOW}{engine}{RESET}")
    print()

    # ── Choose IWAD ──
    iwad_path = choose_iwad()
    print()

    # ── Launch ──
    launch_doom(pwad_path, iwad_path, engine)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f"\n  {DOOM_GRAY}goodby, Doomguy ;).{RESET}\n")
        sys.exit(0)
