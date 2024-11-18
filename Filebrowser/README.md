# To Install 

### On systemd systems

    bash -c "$(wget -qLO - https://github.com/Telxey/Proxmox/raw/main/Filebrowser/install)"

### On Openrc systems ( Alpine )    

    bash -c "$(wget -qLO - https://github.com/Telxey/Proxmox/raw/main/Filebrowser/install_openrc)"

# To update 

    curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

## RUN sh file
1- Download by run below command

    curl -o ~/filebrowser.sh https://github.com/Telxey/Proxmox/raw/main/Filebrowser/filebrowser.sh

  2- Running start stop or status command as needed
  
. Run for start filebrowser

    ~/filebrowser.sh start    
. Run for stop fileBrowser
 
    ~/filebrowser.sh stop
. run for get filebrowser status
    
    ~/filebrowser.sh status
