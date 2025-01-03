Some jank Copilot and I threw together to detect Intel BootGuard. amd support coming when i return to my amd PC and stop being lazy.

In my testing, it required windows to be running baremetal (not hyper-v) to be disabled to prevent bluescreening when reading the MSR. You should probably disable your hypervisor if you encounter this issue.

probably also requires vulnerable driver blocklist disabled cuz it uses RWEverything's driver.

yes its gonna flag windows defender with Trojan:Win32/Malgent.MSR but I could not be bothered to fix, its a one time use info gathering tool.