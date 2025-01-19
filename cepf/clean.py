import os
import sys
import time
import subprocess
from colorama import Fore, Style, init
from shutil import get_terminal_size

# Initialize colorama
init()

# Color definitions
bold = Style.BRIGHT
dim = Style.DIM
reverse = "\033[7m"
hidden = "\033[8m"
normal = Style.RESET_ALL
blue = Fore.BLUE
red = Fore.RED
green = Fore.GREEN
orange = "\033[38;5;202m"
lightblue = "\033[94m"
lightyellow = "\033[38;5;184m"
lightpurple = "\033[38;5;135m"
lightaqua = "\033[96m"
white = Fore.WHITE
default = "\033[39m"
YW = "\033[33m"
BL = "\033[36m"
RD = "\033[01;31m"
BGN = "\033[4;92m"
GN = "\033[1;92m"
DGN = "\033[32m"
CL = "\033[m"
CM = f"{GN}✓{CL}"
CROSS = f"{RD}✗{CL}"
BFR = "\r\033[K"
HOLD = "-"
underline = "\033[4m"

# Links
def show_links():
    print(f"{green}    Links: {normal}")
    print(f"{orange}    ====== {normal}")
    print(f"{lightblue}{bold}    Support:        {green}https://github.com/Telxey/Proxmox/issues {normal}")
    print(f"{lightblue}{bold}    Repository:     {green}https://github.com/Telxey/Proxmox {normal}")
    print(f"{lightblue}{bold}    License:        {green}https://raw.githubusercontent.com/Telxey/Proxmox/main/LICENSE {normal}")

# Progress bar function
def progress_bar(duration):
    cols = get_terminal_size().columns - 10
    for i in range(1, duration + 1):
        progress = i * cols // duration
        print(f"\r[{orange}{'▇' * progress}{' ' * (cols - progress)}{normal}] {i * 100 // duration}%", end="")
        time.sleep(0.1)
    print()

# Interactive spinner
def spinner(pid):
    spinstr = '|/-\\'
    while True:
        for char in spinstr:
            print(f"  [{char}]  ", end="\r")
            time.sleep(0.1)
        if not os.path.exists(f"/proc/{pid}"):
            break
    print("    \b\b\b\b", end="")

# Execute command with spinner
def exec_with_spinner(cmd, msg):
    msg_info(msg)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    spinner(process.pid)
    if process.wait() == 0:
        msg_ok(f"{msg} completed")
    else:
        msg_error(f"{msg} failed")

# Message functions
def msg_info(msg):
    print(f" {HOLD} {YW}{msg}...{CL}", end="")

def msg_ok(msg):
    print(f"{BFR} {CM} {GN}{msg}{CL}")

def msg_error(msg):
    print(f"{BFR} {CROSS} {RD}{msg}{CL}")

# Execute command with progress
def exec_with_progress(cmd, msg):
    msg_info(msg)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    progress_bar(20)
    if process.wait() == 0:
        msg_ok(f"{msg} completed")
    else:
        msg_error(f"{msg} failed")

# Banner functions
def show_banner(text, color, textcolor=None):
    textcolor = textcolor or color
    width = 60
    padding = (width - len(text)) // 2
    print(f"{color}{bold}")
    print("=" * width)
    print(" " * padding + f"{textcolor}{text}{color}")
    print("=" * width)
    print(f"{normal}")

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
        print(f"{red}{bold}{banner}{normal}")
        time.sleep(0.5)
        os.system("clear")
        time.sleep(0.5)

    print(f"{red}{bold}{banner}{normal}")
    print("""
    ⚠️  WARNING: This will completely remove your Ceph installation
    All Ceph storage and configuration will be permanently deleted
    Please ensure you have backups before continuing
    """)
    print(f"{normal}")

def show_ceph_banner():
    print(f"{orange}")
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
    print(f"{normal}")

# Check root
def check_root():
    if os.geteuid() != 0:
        clear()
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

# Info
def show_outro():
    print(f"{white}{bold}")
    print("""
       Thank you for trying this script out.
    """)
    print(f"{normal}")
    time.sleep(5)

# Support Project
def show_support():
    print(f"{orange}{bold}")
    print("""
   Support the Project:
   ==========================================
    """)
    print(f"{normal}{dim}")
    print("""
           🔗 Buy Me a Coffee: https://www.buymeacoffee.com/telxey
    """)
    print(f"{normal}")

# Main cleanup function
def cleanup_ceph():
    # Stop services
    show_banner("Step 1: Stopping Ceph Services", lightblue, orange)
    for service in ["ceph-mon", "ceph-mgr", "ceph-mds", "ceph-osd"]:
        exec_with_spinner(f"systemctl stop {service}.target", f"Stopping {service}")

    # Remove systemd files
    show_banner("Step 2: Removing Systemd Files", lightblue, orange)
    exec_with_spinner("rm -rf /etc/systemd/system/ceph*", "Removing systemd files")
    exec_with_spinner("systemctl daemon-reload", "Reloading systemd")

    # Remove libraries
    show_banner("Step 3: Removing Ceph Libraries", blue, orange)
    exec_with_spinner("rm -rf /var/lib/ceph/mon/ /var/lib/ceph/mgr/ /var/lib/ceph/mds/ /var/lib/ceph/crash/posted/*(N)", "Removing Ceph libraries")

    # Purge packages
    show_banner("Step 4: Purging Ceph Packages", blue, orange)
    exec_with_spinner("pveceph purge", "Purging pveCeph")
    exec_with_spinner("DEBIAN_FRONTEND=noninteractive apt-get purge -y ceph-mon ceph-osd ceph-mgr ceph-mds ceph-base ceph-mgr-modules-core", "Purging Ceph packages")
    exec_with_spinner("DEBIAN_FRONTEND=noninteractive apt-get remove -y ceph-common ceph-fuse", "Removing Ceph components")

    # Remove configs
    show_banner("Step 5: Removing Configurations", blue, orange)
    exec_with_spinner("rm -rf /etc/ceph/* /etc/pve/ceph.conf /etc/pve/priv/ceph.*", "Removing configurations")

    # System cleanup
    show_banner("Step 6: System Cleanup", blue, orange)
    exec_with_spinner("DEBIAN_FRONTEND=noninteractive apt-get autoremove -y", "Running autoremove")
    exec_with_spinner("DEBIAN_FRONTEND=noninteractive apt-get clean", "Cleaning apt cache")
    exec_with_spinner("DEBIAN_FRONTEND=noninteractive apt-get autoclean", "Auto-cleaning packages")
    exec_with_spinner("DEBIAN_FRONTEND=noninteractive apt-get update", "Updating package lists")

    show_banner("Ceph Cleanup Complete!", green, lightyellow)

# Main execution
if __name__ == "__main__":
    os.system("clear")
    msg_info("Checking root")
    time.sleep(5)
    check_root()
    msg_ok("Good to GO ...")
    time.sleep(5)

    os.system("clear")
    show_warning_banner()

    print(f"{orange}{bold}Do you wish to continue removing Ceph?")
    print(f"{green}For continue press 1 {white}{bold} or {red}For cancel press 2 {normal}")
    choice = input("Enter your choice (1 or 2): ")
    if choice != "1":
        print(f"{red}Installation canceled{normal}")
        sys.exit(0)

    os.system("clear")
    show_ceph_banner()
    print(f"{dim}{white}Author: {green}{bold}TELXEY{normal}\n")
    print(f"{lightyellow}Hello{green} Today is: {lightpurple}{time.strftime('%a %b %-d %I:%M:%S %p %Z %Y')}{normal}\n")
    print(f"{underline}\n")
    print(f"{normal}")

    print(f"{green}            Start Cleaning {orange}Ceph")
    print(f"{normal}")

    msg_info("Checking Proxmox Installations")
    pve_check()
    msg_ok("Proxmox is running")
    msg_info("Loading Script")
    msg_ok("Script loaded")

    cleanup_ceph()
    show_outro()
    show_links()
    show_support()

    print(f"\n{green}{bold}Cleanup completed successfully!{normal}")
