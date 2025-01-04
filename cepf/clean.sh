#!/usr/bin/env bash
source <(curl -s https://raw.githubusercontent.com/tteck/Proxmox/main/misc/build.func)
# Copyright (c) 2021-2024 Telxey
# Author: TELXEY (Rax)
# License: MIT
# https://raw.githubusercontent.com/Telxey/Proxmox/main/LICENSE

 bold=`echo -en "\e[1m"`
 dim=`echo -en "\e[2m"`
 blink=`echo -en "\e[5m"`
 reverse=`echo -en "\e[7m"`
 hidden=`echo -en "\e[8m"`
 normal=`echo -en "\e[0m"`
 blue=`echo -en "\e[34m"`
 red=`echo -en "\e[31m"`
 green=`echo -en "\e[32m"`
 orange=`echo -en "\e[33m"`
 lightblue=`echo -en "\e[94m"`
 lightaqua=`echo -en "\e[96m"`
 white=`echo -en "\e[97m"`
 default=`echo -en "\e[39m"`
 YW=$(echo "\033[33m")
 BL=$(echo "\033[36m")
 RD=$(echo "\033[01;31m")
 BGN=$(echo "\033[4;92m")
 GN=$(echo "\033[1;92m")
 DGN=$(echo "\033[32m")
 CL=$(echo "\033[m")
 CM="${GN}✓${CL}"
 CROSS="${RD}✗${CL}"
 BFR="\\r\\033[K"
 HOLD="-"

 # This function displays an informational message with a yellow color.
msg_info() {
  local msg="$1"
  echo -ne " ${HOLD} ${YW}${msg}..."
}

# This function displays a success message with a green color.
msg_ok() {
  local msg="$1"
  echo -e "${BFR} ${CM} ${GN}${msg}${CL}"
}

# This function displays an error message with a red color.
msg_error() {
  local msg="$1"
  echo -e "${BFR} ${CROSS} ${RD}${msg}${CL}"
}

# Run as root only
check_root() {
  if [[ "$(id -u)" -ne 0 || $(ps -o comm= -p $PPID) == "sudo" ]]; then
    clear
    msg_error "Please run this script as root."
    echo -e "\nExiting..."
    sleep 2
    exit
  fi
}
# This function checks the version of Proxmox Virtual Environment (PVE) and exits if the version is not supported.
pve_check() {
  if [ $(pveversion | grep "pve-manager/8" | wc -l) -ne 1 ]; then
    whiptail --backtitle "Proxmox VE Helper Scripts" --msgbox --title "Proxmox VE 7 Detected" "You are currently using Proxmox VE 7 (EOL 2024-07), refrain from creating Debian 12 LXCs. \nDefault distribution for $APP LXC is ${var_os} ${var_version}" 10 60
  fi
  if ! pveversion | grep -Eq "pve-manager/(7\.[0-9]|8\.[0-9])"; then
    echo -e "${CROSS} This version of Proxmox Virtual Environment is not supported"
    echo -e "Requires PVE Version 7.0 or higher"
    echo -e "Exiting..."
    sleep 2
    exit
  fi
} 

# This function is a spiner  that is setup for 10 sec you can ajust the time
spinner=( Ooooooooo oOooooooo ooOoooooo oooOooooo ooooOoooo oooooOooo ooooooOoo oooooooOo ooooooooO);
count(){
  spin &
  pid=$!

  for i in `seq 1 10`
  do
    sleep 0.5;
  done

  kill $pid
  echo ""
}
spin(){
  while [ 1 ]
  do
    for i in ${spinner[@]};
    do
      echo -ne "\r$i";
      sleep 0.2;
    done;
  done
}

# This is solid prosgres bar funtion
progress-bar() {
  local duration=${1}


    already_done() { for ((done=0; done<$elapsed; done++)); do printf "▇"; done }
    remaining() { for ((remain=$elapsed; remain<$duration; remain++)); do printf " "; done }
    percentage() { printf "| %s%%" $(( (($elapsed)*100)/($duration)*100/100 )); }
    clean_line() { printf "\r"; }

  for (( elapsed=1; elapsed<=$duration; elapsed++ )); do
      already_done; remaining; percentage
      sleep 0.25
      clean_line
  done
  clean_line
}


msg_info "Cheking root"
sleep 3
check_root
msg_ok "Good to GO ..."
sleep 3
clear
echo "${red}${bold}${blink}"
cat <<"EOF" 




         ██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
         ██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
         ██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
         ██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
         ╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
          ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝
EOF
echo "${normal}"
echo "${red}${bold}"
cat <<"EOF"

    This is Proxmox cluster ceph cleaner Script due full clean
    wipea and remove all ceph storage funsion file and posible loss 
    sensitive data, Make sure  backup you data, before to continue
EOF
echo "${normal}"
echo "${orange}${bold}Do you wish to continue removing Ceph?"
echo "${green}For continew pree 1 ${white}${bold} or  ${red}For cancel press 2 ${normal}"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) $@; break;;
        No ) echo "${red}Instalations canceled${normal}";  exit;;
    esac
done

echo "${orange}Good loading script ${normal}"
count

clear

echo "${orange}"
cat <<"EOF"

 ▄████▄  ▓█████ ██▓███   ▒ ████▒     ▄████▄   ██▓    ▓█████ ▄▄▄      ███▄    █  ▓█████ ██▀███  
▒██▀ ▀█  ▓█   ▀▓██░  ██ ▒▓██        ▒██▀ ▀█  ▓██▒    ▓█   ▀▒████▄    ██ ▀█   █  ▓█   ▀▓██ ▒ ██▒
▒▓█    ▄ ▒███  ▓██░ ██▓▒░▒████      ▒▓█    ▄ ▒██░    ▒███  ▒██  ▀█▄ ▓██  ▀█ ██▒ ▒███  ▓██ ░▄█ ▒
▒▓▓▄ ▄██ ▒▓█  ▄▒██▄█▓▒ ▒░░▓█▒       ▒▓▓▄ ▄██ ▒██░    ▒▓█  ▄░██▄▄▄▄██▓██▒  ▐▌██▒ ▒▓█  ▄▒██▀▀█▄  
▒ ▓███▀ ▒░▒████▒██▒ ░  ░ ░▒█░       ▒ ▓███▀ ▒░██████▒░▒████▒▓█   ▓██▒██░   ▓██░▒░▒████░██▓ ▒██▒
░ ░▒ ▒  ░░░ ▒░ ▒▓▒░ ░  ░  ▒ ░       ░ ░▒ ▒  ░░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░ ▒░   ▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░
  ░  ▒  ░ ░ ░  ░▒ ░       ░           ░  ▒  ░░ ░ ▒  ░ ░ ░  ░ ░   ▒▒ ░ ░░   ░ ▒░░ ░ ░    ░▒ ░ ▒ 
░           ░  ░░         ░ ░       ░          ░ ░      ░    ░   ▒     ░   ░ ░     ░    ░░   ░ 
░ ░     ░   ░                       ░ ░     ░    ░  ░   ░        ░           ░ ░   ░     ░     

EOF
echo "${dim}${white}Author: ${green}${bold}TELXEY ${normal}"
echo "${lightyellow}Hello${green} Today is: ${lightpurple} `date` "
echo "${normal}"
echo "${white}${underline}"
echo "${normal}"
cat << EOF
    Thank you for trying this script out.
        I will now wait 10 seconds,

EOF
sleep 5
echo "${green}            Start Cleaning ${orange}Ceph"
echo "${normal}"
sleep 5

msg_info "Checking Proxmox Instalations"
pve_check
msg_ok "Proxmox is runing"
msg_info "Loading Script"
msg_ok "Script loaded"
msg_info "Stoping Ceph Services"
echo "${orange}"
systemctl stop ceph-mon.target &> /dev/null; progress-bar 25
msg_ok "ceph-mon Stoped"
echo "${green}"
systemctl stop ceph-mgr.target &> /dev/null; progress-bar 25
msg_ok "ceph-mgr Stoped"
echo "${red}"
systemctl stop ceph-mds.target &> /dev/null; progress-bar 25
msg_ok "ceph-mds Stoped"
echo "${white}"
systemctl stop ceph-osd.target &> /dev/null; progress-bar 25
msg_ok "ceph-osd Stoped"
msg_info "Removing systemd ceph processes"
echo "${orange}"
rm -rf /etc/systemd/system/ceph* &> /dev/null; progress-bar 25
msg_ok "Removed"
msg_info "Kill Remaining Ceph process"
#killall -9 ceph-mon ceph-mgr ceph-mds
msg_ok "Down"
msg_info "Removing Ceph Libraries"
#echo "${red}"${bold}"
rm -rf /var/lib/ceph/mon/  /var/lib/ceph/mgr/  /var/lib/ceph/mds/
msg_ok "Libraries Removed"
msg_info "Purge pveCeph"
echo "${green}"
pveceph purge &>  /dev/null
apt purge -y ceph-mon ceph-osd ceph-mgr ceph-mds &> /dev/null;  progress-bar 50
apt purge -y ceph-base ceph-mgr-modules-core &> /dev/null; progress-bar 50
msg_ok "Purged"
msg_info "Purge Ceph from system"
apt remove -y ceph-common ceph-fuse &> /dev/null; progress-bar 50
msg_ok "Full Ceph removed"
msg_info "Removing Configurations"
msg_info "Type Y to renove Ceph Files"
rm -rf /etc/ceph/*
rm -rf /etc/pve/ceph.conf
rm -rf /etc/pve/priv/ceph.*
msg_ok "Configs Removed"
msg_info "Final System Cleanup & Updated"
apt autoremove -y  &> /dev/null; progress-bar 10
apt clean  &> /dev/null; progress-bar 5
apt autoclean  &> /dev/null; progress-bar 5
apt update  &> /dev/null; progress-bar 10
msg_ok "Process Complete"


