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
 

 
clear
echo "${red}${bold}${blink}"
cat <<"EOF" 




         ██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗ ██████╗ 
         ██║    ██║██╔══██╗██╔══██╗████╗  ██║██║██╔════╝ 
         ██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██║  ███╗
         ██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║   ██║
         ╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║╚██████╔╝
          ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ 
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
        No ) echo "${red}Instalations canceled by root${normal}";  exit;;
    esac
done

echo "${orange}Good loading script ${normal}
count
# 
clear
echo "${dim}${white}Author: ${green}${bold}TELXEY"
echo "$normal"
echo "${orange}
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

pve_check
error_handler
#catch_errors
network_check
update_os

systemctl stop ceph-mon.target
systemctl stop ceph-mgr.target
systemctl stop ceph-mds.target
systemctl stop ceph-osd.target
rm -rf /etc/systemd/system/ceph*
killall -9 ceph-mon ceph-mgr ceph-mds
rm -rf /var/lib/ceph/mon/  /var/lib/ceph/mgr/  /var/lib/ceph/mds/
pveceph purge
apt purge ceph-mon ceph-osd ceph-mgr ceph-mds
apt purge ceph-base ceph-mgr-modules-core
rm -rf /etc/ceph/*
rm -rf /etc/pve/ceph.conf
rm -rf /etc/pve/priv/ceph.*


