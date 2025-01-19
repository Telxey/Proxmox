#!/usr/bin/env python3

import os
import sys
import time
import subprocess
from shutil import get_terminal_size

# Native ANSI color codes
class Colors:
    BOLD = "\033[1m"
    DIM = "\033[2m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    RESET = "\033[0m"
    BLUE = "\033[34m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    ORANGE = "\033[38;5;202m"
    LIGHTBLUE = "\033[94m"
    LIGHTYELLOW = "\033[38;5;184m"
    LIGHTPURPLE = "\033[38;5;135m"
    LIGHTAQUA = "\033[96m"
    WHITE = "\033[97m"
    YELLOW = "\033[33m"
    UNDERLINE = "\033[4m"

# Links
def show_links():
    print(f"{Colors.GREEN}    Links: {Colors.RESET}")
    print(f"{Colors.ORANGE}    ====== {Colors.RESET}")
    print(f"{Colors.LIGHTBLUE}{Colors.BOLD}    Support:        {Colors.GREEN}https://github.com/Telxey/Proxmox/issues {Colors.RESET}")
    print(f"{Colors.LIGHTBLUE}{Colors.BOLD}    Repository:     {Colors.GREEN}https://github.com/Telxey/Proxmox {Colors.RESET}")
    print(f"{Colors.LIGHTBLUE}{Colors.BOLD}    License:        {Colors.GREEN}https://raw.githubusercontent.com/Telxey/Proxmox/main/LICENSE {Colors.RESET}")

# Progress bar function
def progress_bar(duration):
    cols = get_terminal_size().columns - 10
    for i in range(1, duration + 1):
        progress = i * cols // duration
        print(f"\r[{Colors.ORANGE}{'▇' * progress}{' ' * (cols - progress)}{Colors.RESET}] {i * 100 // duration}%", end="")
        time.sleep(0.1)
    print()

# Message functions
def msg_info(msg):
    print(f" - {Colors.YELLOW}{msg}...{Colors.RESET}", end="")

def msg_ok(msg):
    print(f"\r {Colors.GREEN}✓ {msg}{Colors.RESET}")

def msg_error(msg):
    print(f"\r {Colors.RED}✗ {msg}{Colors.RESET}")

# Banner functions
def show_banner(text, color, textcolor=None):
    textcolor = textcolor or color
    width = 60
    padding = (width - len(text)) // 2
    print(f"{color}{Colors.BOLD}")
    print("=" * width)
    print(" " * padding + f"{textcolor}{text}{color}")
    print("=" * width)
    print(f"{Colors.RESET}")

# Warning banner
def show_warning_banner():
    banner = """
     ██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
     ██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
     ██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
     ██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
     ╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
      ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ """

    for _ in range(7):
        os.system("clear")
        print(f"{Colors.RED}{Colors.BOLD}{banner}{Colors.RESET}")
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)

    print(f"{Colors.RED}{Colors.BOLD}{banner}{Colors.RESET}")
    print("""
    ⚠️  WARNING: This will completely remove your Ceph installation
    All Ceph storage and configuration will be permanently deleted
    Please ensure you have backups before continuing
    """)
    print(f"{Colors.RESET}")

# Ceph banner
def show_ceph_banner():
    print(f"{Colors.ORANGE}")
    print("""
 ▄████▄  ▓█████ ██▓███   ▒ ████▒     ▄████▄   ██▓    ▓█████ ▄▄▄      ███▄    █  ▓█████ ██▀███  
▒██▀ ▀█  ▓█   ▀▓██░  ██ ▒▓██        ▒██▀ ▀█  ▓██▒    ▓█   ▀▒████▄    ██ ▀█   █  ▓█   ▀▓██ ▒ ██▒
▒▓█    ▄ ▒███  ▓██░ ██▓▒░▒████      ▒▓█    ▄ ▒██░    ▒███  ▒██  ▀█▄ ▓██  ▀█ ██▒ ▒███  ▓██ ░▄█ ▒
▒▓▓▄ ▄██ ▒▓█  ▄▒██▄█▓▒ ▒░░▓█▒       ▒▓▓▄ ▄██ ▒██░    ▒▓█  ▄░██▄▄▄▄██▓██▒  ▐▌██▒ ▒▓█  ▄▒██▀▀█▄  
▒ ▓███▀ ▒░▒████▒██▒ ░  ░ ░▒█░       ▒ ▓███▀ ▒░██████▒░▒████▒▓█   ▓██▒██░   ▓██░▒░▒████░██▓ ▒██▒
░ ░▒ ▒  ░░░ ▒░ ▒▓▒░ ░  ░  ▒ ░       ░ ░▒ ▒  ░░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░ ▒░   ▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░
  ░  ▒  ░ ░ ░  ░▒ ░       ░           ░  ▒  ░░ ░ ▒  ░ ░ ░  ░ ░   ▒▒ ░ ░░   ░ ▒░░ ░ ░    ░▒ ░ ▒ 
░           ░  ░░         ░ ░       ░          ░ ░      ░    ░   ▒     ░   ░ ░     ░    ░░   ░ 
░ ░     ░   ░                       ░ ░     ░    ░  ░   ░        ░           ░ ░   ░     ░     
    """)
    print(f"{Colors.RESET}")

# Check root
def check_root():
    if os.geteuid() != 0:
        msg_error("Please run this script as root.")
        print("\nExiting...")
        time.sleep(2)
        sys.exit(1)

# Check Proxmox version
def pve_check():
    try:
        pveversion = subprocess.check_output("pveversion", shell=True).decode()
        if "pve-manager/8" not in pveversion:
            print("Proxmox VE 7 Detected: You are currently using Proxmox VE 7 (EOL 2024-07), refrain from creating Debian 12 LXCs.")
        if not ("pve-manager/7." in pveversion or "pve-manager/8." in pveversion):
            msg_error("This version of Proxmox Virtual Environment is not supported")
            print("Requires PVE Version 7.0 or higher")
            print("Exiting...")
            time.sleep(2)
            sys.exit(1)
    except subprocess.CalledProcessError:
        msg_error("Failed to check Proxmox version")
        sys.exit(1)

# Execute command with timeout
def run_command(cmd, timeout=30):
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=timeout)
        return True
    except subprocess.TimeoutExpired:
        msg_error(f"Command timed out: {' '.join(cmd)}")
        return False
    except subprocess.CalledProcessError:
        msg_error(f"Command failed: {' '.join(cmd)}")
        return False

# Main cleanup function
def cleanup_ceph():
    # Stop services
    show_banner("Step 1: Stopping Ceph Services", Colors.LIGHTBLUE, Colors.ORANGE)
    for service in ["ceph-mon", "ceph-mgr", "ceph-mds", "ceph-osd"]:
        msg_info(f"Stopping {service}")
        if run_command(["systemctl", "stop", f"{service}.target"]):
            msg_ok(f"Stopped {service}")
        else:
            msg_error(f"Failed to stop {service}")

    # Remove systemd files
    show_banner("Step 2: Removing Systemd Files", Colors.LIGHTBLUE, Colors.ORANGE)
    msg_info("Removing systemd files")
    if run_command(["rm", "-rf", "/etc/systemd/system/ceph*"]) and run_command(["systemctl", "daemon-reload"]):
        msg_ok("Systemd files removed")
    else:
        msg_error("Failed to remove systemd files")

    # Remove libraries
    show_banner("Step 3: Removing Ceph Libraries", Colors.BLUE, Colors.ORANGE)
    msg_info("Removing Ceph libraries")
    if run_command(["rm", "-rf", "/var/lib/ceph/mon/", "/var/lib/ceph/mgr/", "/var/lib/ceph/mds/", "/var/lib/ceph/crash/posted/*"]):
        msg_ok("Ceph libraries removed")
    else:
        msg_error("Failed to remove Ceph libraries")

    # Purge packages
    show_banner("Step 4: Purging Ceph Packages", Colors.BLUE, Colors.ORANGE)
    msg_info("Purging pveCeph")
    if run_command(["pveceph", "purge"]):
        msg_ok("pveCeph purged")
    else:
        msg_error("Failed to purge pveCeph")

    # Remove configs
    show_banner("Step 5: Removing Configurations", Colors.BLUE, Colors.ORANGE)
    msg_info("Removing configurations")
    if run_command(["rm", "-rf", "/etc/ceph/*", "/etc/pve/ceph.conf", "/etc/pve/priv/ceph.*"]):
        msg_ok("Configurations removed")
    else:
        msg_error("Failed to remove configurations")

    # System cleanup
    show_banner("Step 6: System Cleanup", Colors.BLUE, Colors.ORANGE)
    msg_info("Running autoremove")
    if run_command(["apt-get", "autoremove", "-y"]):
        msg_ok("Autoremove completed")
    else:
        msg_error("Failed to run autoremove")

    show_banner("Ceph Cleanup Complete!", Colors.GREEN, Colors.LIGHTYELLOW)

# Main execution
if __name__ == "__main__":
    check_root()
    pve_check()
    show_warning_banner()
    show_ceph_banner()
    cleanup_ceph()
    show_links()
