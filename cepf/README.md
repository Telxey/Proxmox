</p>
<img align="left" width="250" height="250" src="https://github.com/Telxey/Proxmox/assets/131807761/909846c0-fdbb-43b4-9ee5-0f938eed40ac"> 
<img align="center" width="220" height="220" src="https://github.com/user-attachments/assets/c79f015d-21e3-4a9c-986e-d3573c55b3b4">
</p>


.

##  <span style='color: red;'>Ceph</span> on <span style='color: red;'>Proxmox</span>
#### This is a customized spript to full remove Cepf from Proxmox 
#### in case you make mistake and need to start from scrach

#### Stips

- Stop all Ceph services (Monitoring, Managers, OSDs, MDS) 
- Remove all ceph systemd related processes
- kill remaining backgroud ceft process
- Removing ceph libraries
- pveceph purge
- remove & purge all cepg configurations
- clean system

 run this one click auto clean script 

 ######  ( Bash Version )

    bash -c "$(wget -qLO - https://raw.githubusercontent.com/Telxey/Proxmox/main/cepf/clean)"

 ######  ( Python3 Version )

    python3 <(curl -sSL https://raw.githubusercontent.com/Telxey/Proxmox/main/cepf/clean.py)

-  Thanks for using this Script

<p align="center">
   <a href="https://www.buymeacoffee.com/telxey" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>
