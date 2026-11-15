# Mission 1 — Know your computer

## 1. Task / objective
The goal of Mission 1 is to explore computer fundamentals:
- Trace how data moves through a computer using the Input, Processing, Output, Storage (IPOS) model.
- Classify essential computer components into hardware and software, further categorizing software into operating systems, application software, and utility software.
- Investigate three real-world computer-based systems outside of typical laptops and smartphones.

---

## 2. Work completed

### Task 1.1 — Trace one activity using IPOS
**Chosen activity:** Typing a line of Python code (`print("Hello World")`) in a code editor and saving the file to disk.

| Stage | What happens in your example? | Possible hardware / component |
|---|---|---|
| **Input** | The user presses keys on the keyboard to enter the text `print("Hello World")`. Each keystroke generates an electrical signal translated into a keycode character. | Built-in keyboard, USB keyboard, or trackpad |
| **Processing** | The CPU receives the keyboard interrupt, interprets the keycodes, coordinates with macOS window management, stores the temporary text in RAM, and prepares the graphical pixels to render. | Apple Silicon CPU (M-series / multi-core processor) and RAM (Unified Memory) |
| **Output** | The text characters appear immediately on the monitor display inside the editor window so the user can verify what was typed. | Retina display / external monitor and GPU (graphics processor) |
| **Storage** | When the user presses `Cmd + S` (Save), the text data is transferred from volatile RAM into a file (`hello.py`) on permanent solid-state storage. | Internal SSD (NVMe Solid State Drive) |

#### Explanation of data flow:
1. **Input $\rightarrow$ Memory:** Key presses create electrical signals that keyboard controller firmware converts into scan codes, sent via USB/bus to the operating system.
2. **Processing:** The OS delivers these input events to the text editor process. The CPU places the character bytes into the application's memory buffer in RAM.
3. **Output:** The GPU renders font glyphs into a frame buffer, and the display controller refreshes the screen pixels so the user sees the characters.
4. **Storage:** Upon saving, the filesystem driver writes the memory buffer blocks through the storage controller into non-volatile NAND flash cells on the SSD. Even when the computer is shut down, the file remains intact.

---

### Task 1.2 — Identify hardware and software
Here is a list of four hardware components and four software programs used on my system:

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
|---|---|---|---|
| **Keyboard** | Hardware | Not applicable | Input device used to type commands, code, and text into the computer. |
| **Retina Display (Screen)** | Hardware | Not applicable | Output device that visually presents user interfaces, terminals, and graphics. |
| **Apple Silicon M-Series SoC** | Hardware | Not applicable | Core processing hardware containing the CPU, GPU, Neural Engine, and memory controller. |
| **Solid State Drive (SSD)** | Hardware | Not applicable | Non-volatile secondary storage device that permanently holds the OS, programs, and user files. |
| **macOS** | Software | Operating system software | Manages system resources, hardware interaction, file systems, process scheduling, and security. |
| **Visual Studio Code** | Software | Application software | User application used for writing, editing, and managing code files and projects. |
| **Google Chrome / Safari** | Software | Application software | Web browser application used to access the internet, search information, and view web pages. |
| **Disk Utility** | Software | Utility software | System maintenance utility used to inspect storage health, manage partitions, and repair disk volume errors. |

---

### Task 1.3 — Computer systems around you
Three dedicated computer-based systems encountered in everyday life:

| System | Main purpose | One input | One output |
|---|---|---|---|
| **Automated Teller Machine (ATM)** | Authenticates bank customers, handles secure cash withdrawals, and checks account balances. | Pin-pad keypad or card chip reader | Cash dispenser mechanism or thermal receipt printer |
| **Metro Station Smart Fare Gate** | Validates passenger travel cards or QR tickets and controls physical entry/exit turnstiles. | RFID / NFC card reader | Green/red directional LED indicator and pneumatic gate barrier opener |
| **Smart Traffic Light Controller** | Coordinates traffic flow at road intersections based on vehicle presence and timing logic. | Induction loop sensor embedded in the road pavement | High-luminance red, amber, and green LED signal heads |

---

## 3. Commands / tools used
- **Text Editor:** Used to record observations, draft markdown tables, and organize content.
- **Terminal utilities (`uname`, `sw_vers`):** Used to confirm the hardware platform (Apple Silicon arm64) and operating system version (macOS 27.2).

---

## 4. My understanding
- **The IPOS Cycle:** Every computing task fundamentally relies on receiving input, processing it according to programmed instructions, presenting an output to the user or external system, and saving data to persistent storage if required.
- **Volatile vs. Non-volatile Memory:** RAM is volatile working memory needed for real-time CPU processing; if the power goes out before saving, anything held only in RAM is lost. Storage (SSD) is non-volatile and preserves data permanently across restarts.
- **Software Categories:** 
  - *Operating System:* Acts as the bridge between raw hardware and user programs (e.g., macOS, Linux, Windows).
  - *Application Software:* Programs built to perform specific tasks for the user (e.g., VS Code, web browsers).
  - *Utility Software:* Tools designed to maintain, optimize, diagnose, or protect the computer system itself (e.g., Disk Utility, Activity Monitor).
- **Embedded / Dedicated Systems:** Computers exist in many forms outside of personal computers. Systems like ATMs and traffic controllers use specialized microcontrollers or embedded PCs with dedicated input sensors and output actuators to perform one specific job reliably.

---

## 5. Difficulties faced
- Initially deciding whether RAM belongs under "Processing" or "Storage" in the IPOS model.
- Distinguishing between application software and utility software for pre-installed tools.

---

## 6. How I resolved them
- Clarified that in standard IPOS definitions, RAM is part of the active working memory used directly by the CPU during processing, whereas "Storage" specifically refers to persistent secondary storage (like SSDs or HDDs).
- Defined utilities as tools that assist the operating system in managing or maintaining the system itself (such as Disk Utility), while applications serve direct end-user productivity tasks.

---

## 7. Evidence / files
- Updated documentation: `mission-01-computer-basics/README.md`
- Completed tables: IPOS Trace (Task 1.1), Hardware & Software Classification (Task 1.2), Everyday Systems (Task 1.3).

---

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Target branch:** `main`
- **Remote status:** Ready to stage, commit, and push to GitHub origin.
