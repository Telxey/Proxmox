
<h1 align="center">
   $${\color{aqua}Using \space Open \space vSwitch \space in \space \color{darkorange} Proxmox.}$$
</h1>

<h3 align="center">Install OvS (Open vSwitch) on Proxmox</h3>

    bash -c "$(wget -qLO - https://raw.githubusercontent.com/Telxey/Proxmox/main/system-tools/Open_vSwitch/OvS)"


<p align="center">
   <a href="https://www.buymeacoffee.com/telxey" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-yellow.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>

***

By default, Proxmox uses Linux Bridges.  For single LPAR using a small MTU size: Open vSwitch is recommended over the Linux bridge. The Linux bridge falls behind Open vSwitch across most tests for throughput and transaction time (latency), where the most notable difference was observed with large transactional payloads.

<br /><p align="center">
  ${\color{aqua}{1.\color{red} \space Important: \color{aqua} \space Create \space a \space backup \space of \space the \space current \space network \space configuration \space If \space you \space ran \space Install \space OvS script before \space you \space have \space backup}}$
</p><br />

Open the shell from the web console. This is the same shell as if you are sitting in front of the server.

And, run this command:

    cp /etc/network/interfaces /etc/network/interfaces.bak
    
<h1 align="center">
   $${\color{aqua}Network \space Configurations \space steps.}$$
</h1>


 <h3 align="center">⚠️ Warning: DO NOT click "Apply Setting" until the following steps are completed.</h3>

<br /><p align="left">
  ${\color{aqua}{2. \space Remove \space the \space Linux \space Bridge}}$
</p><br />

Click on your [Proxmox Node] > Network. Select vmbr0 and choose Remove.


<br /><p align="left">
  ${\color{aqua}{3. \space Create \space the \space Open \space vSwitches}}$
</p><br />

Click Create > OVS Bridge (A bridge is another name for a vSwitch)

Fill out the fields exactly like this and click Create. Note that my physical interface on my laptop has the name enp0s31f6. Fill in this field with your physical interface name.


<br /><p align="left">
  ${\color{aqua}{3. \space Create \space the \space Management \space Interface}}$
</p><br />

Click Create > OVS IntPort. An IntPort is a way to create VLANs.

Fill it out and click Create. Make sure you enter your Proxmox node’s IP address – not mine. The Proxmox web console IP address gets its own IntPort. This is will ensure that you can log into the web console.

