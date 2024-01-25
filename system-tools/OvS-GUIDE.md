<h1 align="center">
   $${\color{aqua}Using \space Open \space vSwitch \space in \space \color{darkorange} Proxmox.}$$
</h1>

<p align="center">
   <a href="https://www.buymeacoffee.com/telxey" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-black.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>

***

By default, Proxmox uses Linux Bridges.  For single LPAR using a small MTU size: Open vSwitch is recommended over the Linux bridge. The Linux bridge falls behind Open vSwitch across most tests for throughput and transaction time (latency), where the most notable difference was observed with large transactional payloads.
