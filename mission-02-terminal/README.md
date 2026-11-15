# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to develop practical fluency with the command-line interface (CLI) on macOS:
- Explore fundamental navigation and file-management commands (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
- Safely practise creating, modifying, appending, copying, and renaming files inside an isolated `terminal-practice/` directory.
- Understand how command options/flags (`-l`, `-a`, `-h`) alter command behavior.
- Understand the pipeline operator (`|`) by chaining a detailed directory listing into `head`.
- Inspect the system package manager (Homebrew) and explain its role in software management.

---

## 2. Work completed

### Task 2.1 — Basic Terminal operations
Inside the repository root, each command was run and observed:

| Operation / command name | What it does | What I observed |
|---|---|---|
| **Current-directory display** (`pwd`) | Prints the full absolute path of the active working directory. | Displayed `/Users/[redacted]/Desktop/digital-detective-8430`. |
| **Directory listing** (`ls`) | Lists visible files and directories in the current folder. | Displayed repository folders (`README.md`, `mission-00-setup`, `terminal-practice`, etc.). |
| **Detailed listing** (`ls -l`) | Displays entries in long format with permissions, owner, file size, and timestamp. | Output showed column headers, file modes (`-rw-r--r--`, `drwxr-xr-x`), sizes in bytes, and update dates. |
| **Change directory** (`cd ..` then `cd digital-detective-8430`) | Changes the current shell location to the specified directory. | Navigated up to the parent directory (`..`), verified with `pwd`, and returned into `digital-detective-8430`. |
| **Create directory** (`mkdir terminal-practice`) | Creates a new folder at the specified target path. | Created the dedicated practice folder without producing extra output (silent success). |
| **Create empty file** (`touch terminal-practice/sample.txt`) | Creates an empty file or updates the timestamp of an existing file. | A new 0-byte file `sample.txt` was created in `terminal-practice/`. |
| **Copy file** (`cp terminal-practice/sample.txt terminal-practice/sample_backup.txt`) | Duplicates a source file to a destination file path. | Created an identical second file `sample_backup.txt` alongside `sample.txt`. |
| **Move / rename file** (`mv terminal-practice/sample_backup.txt terminal-practice/archived_sample.txt`) | Moves a file to a new path or renames it in place. | Renamed `sample_backup.txt` to `archived_sample.txt`; the old filename ceased to exist. |
| **Display file contents** (`cat terminal-practice/sample.txt`) | Reads the contents of a file and prints it directly to terminal standard output. | Displayed the text stored inside `sample.txt`. |

---

### Task 2.2 — Practise file changes safely
All file experiments were performed strictly inside `terminal-practice/`:

1. Created `sample.txt` and wrote the first line using the redirection operator `>`:
   ```bash
   echo "First line: Exploring Terminal commands" > terminal-practice/sample.txt
   ```
2. Appended a second line without removing the first line using the append operator `>>`:
   ```bash
   echo "Second line: Appending text without overwriting" >> terminal-practice/sample.txt
   ```
3. Verified both lines using `cat`:
   ```text
   $ cat terminal-practice/sample.txt
   First line: Exploring Terminal commands
   Second line: Appending text without overwriting
   ```
4. Copied `sample.txt` to `sample_backup.txt` and renamed it to `archived_sample.txt` using `mv`.

#### Questions & Answers:
- **What is the difference between replacing a file's contents and adding text to the end?**  
  The single chevron redirection operator `>` truncates (overwrites) the target file, replacing whatever was previously inside it with the new output. The double chevron operator `>>` appends new text to the end of the file, preserving all existing lines.
- **What is the difference between copying a file and moving a file?**  
  Copying (`cp`) creates a new duplicate file on disk, resulting in two independent files that occupy separate storage blocks. Moving (`mv`) renames the file or relocates its directory pointer in the filesystem table, leaving only one file at the new location without duplicating data blocks.
- **What information does the current-directory display provide?**  
  The `pwd` command outputs the exact absolute path from the filesystem root (`/`) down to the directory the shell session is currently positioned in. This prevents accidental execution of commands in the wrong location.
- **Why is a directory-listing operation useful?**  
  `ls` gives visibility into what files and subdirectories are present, verifying their existence, spelling, file sizes, and modification timestamps before attempting to read, modify, or execute them.

---

### Task 2.3 — Understand flags and pipes

#### Flags comparison:
- `ls`: Shows only basic names in multi-column format.
- `ls -l`: Long format showing permissions, link count, owner, group, size in bytes, modification date/time, and name.
- `ls -lah`: 
  - `-l`: Long listing format.
  - `-a`: Includes hidden files and directories (those starting with `.`, such as `.git` and `.`).
  - `-h`: Human-readable file sizes (e.g., displaying `88B`, `480B`, `4.1K` instead of raw byte counts).

**Observed output in `terminal-practice/`:**
```text
$ ls -lah terminal-practice
total 16
drwxr-xr-x@  4 [redacted]  staff   128B Nov 16 03:51 .
drwxr-xr-x@ 15 [redacted]  staff   480B Nov 16 03:51 ..
-rw-r--r--@  1 [redacted]  staff    88B Nov 16 03:51 archived_sample.txt
-rw-r--r--@  1 [redacted]  staff    88B Nov 16 03:51 sample.txt
```

#### Pipes (`|`):
We piped the output of a detailed directory listing into `head`:
```bash
ls -la | head -n 5
```
**Observed output:**
```text
total 8
drwxr-xr-x@  15 [redacted]  staff   480 Nov 16 03:51 .
drwx------+ 129 [redacted]  staff  4128 Nov 16 03:38 ..
drwxr-xr-x@  12 [redacted]  staff   384 Nov 16 03:50 .git
-rw-r--r--@   1 [redacted]  staff  3770 Nov 16 03:50 README.md
```
- **How the pipe works:** The vertical pipe symbol `|` takes the standard output (`stdout`) of the command on its left (`ls -la`) and feeds it directly as standard input (`stdin`) to the command on its right (`head -n 5`).
- **Contribution of each side:** 
  - Left side (`ls -la`): Generates the complete detailed directory stream.
  - Right side (`head -n 5`): Reads that incoming stream and truncates it, printing only the first 5 lines to the screen.

---

### Task 2.4 — Understand package managers
Checked package manager on macOS:
```text
$ brew --version
Homebrew 7.0.13
```
- **Observed packages:** Homebrew is installed and manages tools such as `python@3.14`, `git`, `htop`, `node`, `ripgrep`, and libraries like `openssl` and `sqlite`.
- **Why package managers are useful:**  
  A package manager automates finding, downloading, compiling, installing, configuring, and updating software tools directly from the command line. Instead of manually searching websites for installers, dragging files to Applications, and resolving conflicting library dependencies, a single command (like `brew install <tool>` or `apt install <tool>`) safely installs the tool and all supporting packages it requires.

---

## 3. Commands / tools used
- `pwd`: Displayed absolute path of current folder.
- `ls`, `ls -l`, `ls -lah`: Explored directory listings, hidden files, and readable size units.
- `cd`: Navigated between folders.
- `mkdir`: Created `terminal-practice` folder.
- `touch`: Created initial text files.
- `echo` with `>` and `>>`: Demonstrated overwriting vs. appending text.
- `cat`: Printed file contents to terminal.
- `cp`: Cloned file to backup copy.
- `mv`: Renamed backup file to archived name.
- `|` (pipe) with `head -n 5`: Filtered multi-line terminal stream.
- `brew --version` & `brew list`: Inspected Homebrew package manager.

---

## 4. My understanding
- The command-line interface provides precise, scriptable control over the computer without needing a graphical window manager or Finder.
- Redirection operators are powerful: `>` creates/overwrites while `>>` preserves existing data.
- The UNIX philosophy of combining small, focused tools using pipes (`|`) allows complex data processing workflows from simple building blocks.
- Package managers keep development environments organized and reproducible.

---

## 5. Difficulties faced
- Accidentally using `>` when intending to append would erase existing contents, so paying attention to `>` vs `>>` is critical.
- Understanding the difference between relative paths (`terminal-practice/sample.txt`) and absolute paths (`/Users/.../terminal-practice/sample.txt`).

---

## 6. How I resolved them
- Practised using `cat` immediately after redirection commands to inspect file contents and confirm both lines were intact.
- Observed how `pwd` helps anchor relative paths to the current directory.

---

## 7. Evidence / files
- Mission documentation: `mission-02-terminal/README.md`
- Practice directory and files:
  - `terminal-practice/sample.txt`
  - `terminal-practice/archived_sample.txt`

---

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Target branch:** `main`
- **Remote status:** Ready to stage, commit, and push to GitHub origin.
