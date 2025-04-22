# To Install 

### On systemd systems

#### To run on default port ( IP:8080 )

    bash -c "$(wget -qLO - https://github.com/Telxey/Proxmox/raw/main/Filebrowser/install)"
#### To run in custom port ( IP:80808 )  

    bash -c "$(wget -qLO - https://github.com/Telxey/Proxmox/raw/main/Filebrowser/install.sh)"


### On Openrc systems ( Alpine )    

    bash -c "$(wget -qLO - https://github.com/Telxey/Proxmox/raw/main/Filebrowser/install_openrc)"

# To update 

    curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

