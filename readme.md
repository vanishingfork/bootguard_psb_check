Some jank Copilot and I threw together to detect Intel BootGuard.

In my testing, it required windows to be running baremetal (not hyper-v) to be disabled to prevent bluescreening when reading the MSR. You should probably disable your hypervisor if you encounter this issue.

probably also requires vulnerable driver blocklist disabled cuz it uses RWEverything's driver.