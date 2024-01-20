<h1 align="center">
   $${\color{aqua}Hi \space 👋, \space Here \space have \space collections \space of \space scripts \space to \space optimised \space \color{darkorange} Proxmox.}$$
</h1>

<p align="center">
   <a href="https://www.buymeacoffee.com/telxey" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-black.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>

***

<h2 align="center">
  $${\color{darkorange}Proxmox \space VE \space \color{gray} - \space \color{red}Post \space Install}$$
</h2>

<p align="center">
This script provides options for managing Proxmox VE repositories, including disabling the Enterprise Repo, adding or correcting PVE sources, enabling the No-Subscription Repo, adding the test Repo, disabling the subscription nag, updating Proxmox VE, and rebooting the system.
</p>
Run the command below in the Proxmox VE Shell.

      bash -c "$(wget -qLO - https://raw.githubusercontent.com/Telxey/Proxmox/main/setup/post-install)"

<h2 align="center">
  $${\color{darkorange}Proxmox \space VE \space \color{gray} - \space \color{red}Kernel \space Clean}$$
</h2>

<p align="center">
Kernel Clean Remove old Kernels from system
Cleaning unused kernel images is beneficial for reducing the length of the GRUB menu and freeing up disk space. By removing old, unused kernels, the system is able to conserve disk space and streamline the boot process.
</p>
Run the command below in the Proxmox VE Shell.

      bash -c "$(wget -qLO  - https://raw.githubusercontent.com/Telxey/Proxmox/main/setup/kernel-clean)"


<h2 align="center">
  $${\color{darkorange}Proxmox \space VE \space \color{gray} - \space \color{red}Processor \space Microcode}$$
</h2>
<h3 align="center">
  $${\color{aqua}For \space \color{blue} INTEL \space \color{aqua} or \space \color{red}AMD \space \color{aqua} Prossesors}$$
</h3>

<p align="center">
Kernel Clean Remove old Kernels from system
Cleaning unused kernel images is beneficial for reducing the length of the GRUB menu and freeing up disk space. By removing old, unused kernels, the system is able to conserve disk space and streamline the boot process.
</p>
Run the command below in the Proxmox VE Shell.

      bash -c "$(wget -qLO  - https://raw.githubusercontent.com/Telxey/Proxmox/main/setup/microcode)"


 ---
 <h3 align="right">Support:</h3>
<p><a href="https://www.buymeacoffee.com/telxey"> <img align="right" src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" height="45" width="180" alt="telxey" /></a></p><br><br> 
     
