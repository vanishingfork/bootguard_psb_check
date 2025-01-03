Some jank Copilot and I threw together to detect Intel BootGuard. AMD support is untested. Testing will occur some time when I have access to my AMD hardware.

In my testing, the tool requires windows to be running baremetal (not hyper-v) to prevent bluescreening when reading the MSR. You should probably disable any hypervisors you are running under if you encounter this issue.

Probably also requires vulnerable driver blocklist disabled because it uses RWEverything's driver.

Windows Defender will complain about Trojan:Win32/Malgent.MSR but I could not be bothered to fix, its a one time use info gathering tool.