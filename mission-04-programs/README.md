# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to explore how computer programs are translated and executed by the system:
- Write and run a standalone Python script (`hello.py`) from the macOS Terminal using Python 3.
- Compare the two primary program translation mechanisms: compilers and interpreters.
- Understand how modern languages often combine compilation and interpretation in hybrid runtimes.

---

## 2. Work completed

### Task 4.1 — Create and run a Python program
1. Created `mission-04-programs/hello.py` with the following content:
   ```python
   print("Hello from Python")
   ```
2. Executed the program using `python3` from Terminal:
   ```bash
   python3 mission-04-programs/hello.py
   ```
3. Verified the actual output:
   ```text
   Hello from Python
   ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
|---|---|---|
| **When translation / execution happens** | Translates the entire source code file all at once into machine code before the program is executed (Ahead-of-Time / AOT). | Translates and executes instructions line-by-line or statement-by-statement dynamically at runtime. |
| **Typical output** | A standalone executable binary file (e.g., `.exe`, `.out`, or Mach-O binary on macOS) stored on disk. | Immediate program output displayed directly in the shell/terminal, without producing an independent native binary file. |
| **One example** | C, C++, or Rust (using compilers like `clang` or `gcc`). | Python (CPython), Ruby, or JavaScript. |
| **One advantage** | Maximum runtime execution speed and CPU performance optimization, because translation has already occurred prior to running. | Greater flexibility, rapid testing, easier debugging, and portability across different platforms without recompiling. |

#### Detailed Explanation:
A compiler processes the complete program source code upfront and converts it into native machine code (binary instructions of 0s and 1s) tailored directly to the computer's CPU architecture. Because the CPU can execute this binary directly, compiled programs run very quickly, but modifying the code requires a full re-compilation step before seeing results. 

In contrast, an interpreter reads high-level source instructions and carries them out on the fly while the program is running. If an error occurs on line 10, the interpreter will successfully run lines 1 through 9 before halting, which makes development and debugging much faster. 

Many modern programming languages utilize a **hybrid approach**. For example, standard Python (CPython) first compiles source code into an intermediate format called **bytecode** (often saved as `.pyc` files in `__pycache__`), and then the Python Virtual Machine (PVM) interprets that bytecode instruction-by-instruction. Similarly, Java compiles source code into bytecode that a Just-In-Time (JIT) compiler translates into machine code at runtime.

---

## 3. Commands / tools used
- `python3`: Invoked the Python 3.14.7 interpreter to run the script.
- Command executed: `python3 mission-04-programs/hello.py`.
- Text Editor: Used to create and save the `hello.py` source script.

---

## 4. My understanding
- Computers cannot execute human-readable text directly; all code must eventually be translated into binary CPU machine instructions.
- Compilers translate ahead of time for raw speed, while interpreters translate at runtime for rapid feedback and cross-platform flexibility.
- Python is primarily an interpreted language from a user's perspective, but under the hood, it relies on an efficient two-step process: compiling to bytecode, followed by interpretation in a virtual machine.

---

## 5. Difficulties faced
- Ensuring the file was executed using `python3` rather than default `python` (which on older macOS systems was Python 2 or missing).
- Understanding why Python generates `.pyc` cache files if it is classified as an interpreted language.

---

## 6. How I resolved them
- Confirmed the explicit alias `python3` in Terminal, matching Python 3.14.7.
- Researched bytecode execution and clarified the distinction between pure interpreters and virtual machine bytecode interpreters.

---

## 7. Evidence / files
- Python program: `mission-04-programs/hello.py`
- Mission documentation: `mission-04-programs/README.md`
- Terminal execution output:
  ```text
  $ python3 mission-04-programs/hello.py
  Hello from Python
  ```

---

## 8. Commit details
- **Commit message:** `Compare compilers and interpreters`
- **Target branch:** `main`
- **Remote status:** Ready to stage, commit, and push to GitHub origin.
