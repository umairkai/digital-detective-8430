# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 is to investigate the internal architecture and responsibilities of the operating system (OS):
- Explore core system attributes (OS kernel details, account identity, storage capacity, and active processes).
- Understand process concepts, process identifiers (PIDs), and how the OS coordinates background and foreground tasks.
- Analyze filesystem paths (absolute vs. relative) and UNIX file permission strings (`rwx`).
- Detail the six primary responsibilities of an operating system with clear real-world examples.

---

## 2. Work completed

### Task 3.1 — Explore your operating system
Using macOS Terminal, system details were inspected and recorded in a privacy-safe manner:

| Information explored | What it tells you | Your observation (privacy-safe) |
|---|---|---|
| **Operating system / system details** (`uname -srm`, `sw_vers`) | Identifies the OS name, kernel version, build architecture, and release version. | macOS 27.2 (Build 26B123), Darwin Kernel Version 27.2.0, ARM64 architecture (Apple Silicon). |
| **Current account identity** (`whoami`, `id`) | Identifies the active user account and group permissions running the shell session. | User: `[redacted-user]`, primary group: `staff` (standard non-root user). |
| **Available and used storage** (`df -h /`) | Reports the mounted root filesystem size, used space, available free space, and capacity percentage. | Filesystem size: `926 GiB`, Used: `13 GiB`, Available: `713 GiB` (2% disk space utilized on APFS container). |
| **System activity snapshot** (`ps`, `top`) | Displays running system processes, active daemons, CPU time consumed, and process states. | Active macOS launch system with PID 1 (`/sbin/launchd`) and core background daemons (`logd`, `configd`, `powerd`). |

---

### Task 3.2 — Understand processes

#### Key Concepts:
- **What is a process?**  
  A process is an active, running instance of a program in execution. When a program file stored on an SSD is opened, the operating system loads its executable machine code and resources into RAM, creates address space, allocates system descriptors, and schedules it for CPU execution.
- **What does the PID column represent?**  
  The PID (Process Identifier) is a unique integer assigned by the operating system kernel to identify and track each running process. The OS uses PIDs to manage process priorities, allocate resources, and signal or terminate programs.
- **Two examples of processes running on my system:**
  1. `/sbin/launchd` (**PID 1**): The initial root supervisor process on macOS that boots the operating system and manages all background daemons and user sessions.
  2. `/usr/libexec/configd` (**PID 545**): The macOS system configuration daemon responsible for monitoring network interfaces, IP addresses, and connectivity states.

**Observed process sample:**
```text
  PID STAT      TIME COMM
    1 Rs    65:40.76 /sbin/launchd
  531 Ss    34:38.24 /usr/libexec/logd
  536 Ss    14:28.98 /System/Library/.../fseventsd
  545 Ss     5:11.47 /usr/libexec/configd
  547 Ss     4:40.29 /System/Library/.../powerd
```

---

### Task 3.3 — Understand paths and permissions

#### Absolute vs. Relative Paths:
- **Absolute Path:** The complete, unambiguous location of a file or folder starting from the filesystem root directory (`/`). It works identically regardless of the user's current directory.  
  *Example:* `/Users/[redacted-user]/Desktop/digital-detective-8430/terminal-practice/sample.txt`
- **Relative Path:** A path that specifies a file or folder location relative to the shell's active working directory (`pwd`).  
  *Example:* When inside the repository root, the relative path is `terminal-practice/sample.txt`. When inside `mission-03-operating-system/`, the relative path is `../terminal-practice/sample.txt`.

#### File Permissions Analysis:
Examining `terminal-practice/sample.txt`:
```text
$ ls -l terminal-practice/sample.txt
-rw-r--r--@ 1 [redacted-user]  staff  88 Nov 16 03:51 terminal-practice/sample.txt
```

Breaking down the permission string `-rw-r--r--`:
- Position 1 (`-`): Regular file (`d` would denote a directory).
- Positions 2–4 (`rw-`): **Owner permissions** — The file owner can **read** (`r`) and **write** (`w`), but does not have **execute** (`x`) permission.
- Positions 5–7 (`r--`): **Group permissions** — Members of the `staff` group can only **read** the file.
- Positions 8–10 (`r--`): **Others permissions** — Any other user account on the computer can only **read** the file.

| Permission | Meaning | Example |
|---|---|---|
| **r — Read** | Allows the file's contents to be opened and viewed. | Opening a text file or viewing source code in an editor. |
| **w — Write** | Allows the file's contents to be modified, edited, appended, or truncated. | Saving updates to a document or code script. |
| **x — Execute** | Allows the file to be executed as a program or script by the CPU; on a directory, allows entering/traversing the directory. | Running a shell script (`./run.sh`) or navigating into a folder (`cd`). |

---

### Task 3.4 — Operating system responsibilities

| OS responsibility | Your explanation | Example |
|---|---|---|
| **Process management** | The OS creates, schedules, prioritizes, and terminates processes, distributing CPU execution time across multiple tasks so they run concurrently without conflict. | macOS scheduler allocating CPU cycles between a web browser playing video and a background code compilation. |
| **Memory management** | The OS allocates chunks of RAM to active programs, tracks which bytes are in use, prevents programs from overwriting each other's memory, and swaps data to disk (virtual memory) when RAM is full. | Allocating 400 MB of RAM when opening VS Code and reclaiming that memory when the application is closed. |
| **Device management** | The OS communicates with hardware devices (keyboards, displays, printers, SSDs) through specialized software called device drivers, providing a standard interface for applications. | Sending print data through a printer driver over USB or Wi-Fi to print a document. |
| **File management** | The OS organizes data into files and folders, manages storage blocks on disk volumes (using filesystems like APFS or ext4), and enforces read/write permissions. | Creating a new directory `terminal-practice/` and recording its metadata in the APFS filesystem table. |
| **User interface / shell** | The OS provides an interface through which humans can control the computer, either graphically (GUI) or through command interpreters (CLI / shell). | Using the `zsh` Terminal shell to type commands or using macOS Finder to drag files between folders. |
| **Security and permissions** | The OS authenticates user credentials, protects files from unauthorized access through permission flags, and isolates process memory to prevent malicious interference. | Requiring Touch ID / password before modifying system settings, and restricting read access on private user files. |

---

## 3. Commands / tools used
- `uname -srm`: Inspected operating system name, kernel release, and hardware architecture.
- `sw_vers`: Queried macOS product name, version, and build number.
- `whoami` & `id`: Verified active user username and group memberships.
- `df -h /`: Checked disk capacity, used storage, and available storage in human-readable units.
- `ps -ax -o pid,stat,time,comm`: Examined the process table, PIDs, and system daemons.
- `ls -l`: Inspected file permissions and ownership bits.

---

## 4. My understanding
- The operating system is the essential foundation of computing; without it, applications would have to manage raw hardware and memory registers manually.
- Processes are independent units of execution, and PIDs allow both the OS and users to track and control them.
- File permissions (`rwx`) protect the integrity of the filesystem and prevent accidental or unauthorized modifications.
- Absolute paths are reliable anchors, while relative paths enable portable scripts that work within self-contained project directories.

---

## 5. Difficulties faced
- Interpreting the 10-character UNIX file permission string and identifying which character set applies to the owner vs. group vs. others.
- Redacting sensitive user account paths and hostnames from terminal logs while preserving technical accuracy.

---

## 6. How I resolved them
- Divided the permission string into distinct blocks of three characters (`rwx` for owner, group, and others) and referenced standard POSIX permissions tables.
- Applied systematic redactions (`[redacted-user]`, `[redacted-macbook]`) across all logs.

---

## 7. Evidence / files
- Mission documentation: `mission-03-operating-system/README.md`
- Referenced practice file: `terminal-practice/sample.txt`

---

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Target branch:** `main`
- **Remote status:** Ready to stage, commit, and push to GitHub origin.
