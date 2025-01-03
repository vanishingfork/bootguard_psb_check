import os
import sys
import subprocess
import re
import platform

#some jank copilot added cuz it wanted to because it made the script needlessly complicated to begin with.
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return os.path.join(os.path.dirname(__file__), relative_path)

def get_cpu_vendor():
    cpu_info = platform.processor()
    if "Intel" in cpu_info:
        return "INTEL"
    elif "AMD" in cpu_info:
        return "AMD"
    return "UNKNOWN"

def check_amd_psb():
    print("AMD Platform Secure Boot check not implemented")

def check_intel_bootguard():
    rw_path = resource_path("RW.exe")
    command_output = subprocess.run(
        [rw_path, "/Min", "/Nologo", "/Stdout", "/Command=RDMSR 0x13A"],
        capture_output=True, text=True
    )
    lines = command_output.stdout.splitlines()
    if not lines:
        print("No output from RW.exe.")
        return

    match = re.search(r"EDX\) = (0x[\da-f]+).+EAX\) = (0x[\da-f]+)", lines[0], re.I)
    if match:
        combined_val = (int(match.group(1), 16) << 32) | int(match.group(2), 16)
        print(f"Combined 64-bit MSR: {combined_val:#018x}")
        mask = combined_val & 0x30000000
        if mask == 0x0:
            print("BootGuard not enabled")
        elif mask == 0x10000000:
            print("BootGuard verified boot is enabled")
        elif mask == 0x20000000:
            print("BootGuard measured boot is enabled")
        elif mask == 0x30000000:
            print("BootGuard verified + measured boot is enabled")
        else:
            print("Unknown BootGuard setting")
    else:
        print("Could not parse EDX/EAX.")

if __name__ == "__main__":
    vendor = get_cpu_vendor()
    print(f"Detected CPU Vendor: {vendor}")
    
    if vendor == "INTEL":
        check_intel_bootguard()
    elif vendor == "AMD":
        check_amd_psb()
    else:
        print("Unsupported CPU vendor")
        
    input("Press Enter to exit...")