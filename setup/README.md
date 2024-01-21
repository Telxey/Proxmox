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

<p align="center">
After a reboot, you can check whether any microcode updates are currently in effect by running the following command.
</p>

    journalctl -k | grep -E "microcode" | head -n 1


<h2 align="center">
  $${\color{darkorange}Proxmox \space VE \space \color{gray} - \space \color{red}CPU \space Scaling \space Governor.}$$
</h2>

<p align="center">
The CPU scaling governor determines how the CPU frequency is adjusted based on the workload, with the goal of either conserving power or improving performance. By scaling the frequency up or down, the operating system can optimize the CPU usage and conserve energy when possible. For more info click below
</p>   
<h3 align="center">
<p><a href="https://www.kernel.org/doc/html/latest/admin-guide/pm/cpufreq.html?#generic-scaling-governors">CPU Scaling Governors Performance Documentation</a></p><br><br>
</h3>
   Run the command below in the Proxmox VE Shell.

    bash -c "$(wget -qLO  - https://raw.githubusercontent.com/Telxey/Proxmox/main/setup/cpu-scaling)"    


 ---
 <h3 align="right">Support:</h3>
<p><a href="https://www.buymeacoffee.com/telxey"> <img align="right" src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" height="45" width="180" alt="telxey" /></a></p><br><br> 
     
