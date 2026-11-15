# Mission 0 — Repository and Workspace Setup

## 1. Task / objective
The objective of Mission 0 is to set up a clean, structured workspace for the Digital Detective assignment. This includes:
- Checking that required developer tools (Python 3 and Git) are installed and recording their versions.
- Creating the project folder following the mandatory naming rule (`digital-detective-XXXX`, where `XXXX` represents the last four digits of my USN).
- Initializing a local Git repository.
- Setting up the required folder structure for all nine missions (Missions 0 to 8) and the `evidence/` folder.
- Creating a root `README.md` with project information and a mission index.
- Connecting the local repository to GitHub and making the first commit.

## 2. Work completed
- Confirmed the repository name as `digital-detective-8430`.
- Verified local installation of Python 3 and Git using Terminal commands.
- Initialized a Git repository on branch `main`.
- Created folders for all missions:
  - `mission-00-setup/`
  - `mission-01-computer-basics/`
  - `mission-02-terminal/`
  - `mission-03-operating-system/`
  - `mission-04-programs/`
  - `mission-05-numbers-data/`
  - `mission-06-git-github/`
  - `mission-07-networking/`
  - `mission-08-final-report/`
  - `evidence/`
- Created initial Markdown files and root `README.md`.
- Documented tools, folder hierarchy, and repository concepts.

## 3. Commands / tools used
- `python3 --version`: Checked the installed Python 3 interpreter version (`Python 3.14.7`).
- `git --version`: Checked the installed Git version (`git version 2.54.0 (Apple Git-157)`).
- `brew --version`: Verified package manager availability (`Homebrew 7.0.13`).
- `pwd`: Confirmed the current working directory (`/Users/[redacted]/Desktop/digital-detective-8430`).
- `mkdir -p`: Created all required mission directories in one command.
- `git init`: Initialized the local Git tracking system.
- `git status`: Checked untracked files and working tree status.

## 4. My understanding
- **What is a Git repository?**  
  A repository (or "repo") is a storage space where Git tracks all files and folders of a project, along with the complete history of changes over time. It allows me to make changes safely, record meaningful milestones as commits, and revert mistakes if necessary.
- **Why organize the folder structure by mission?**  
  Dividing the project into mission-specific folders (`mission-00` through `mission-08`) keeps each topic self-contained and modular. It prevents file clutter, ensures that exercises and scripts do not interfere with each other, and makes it easy for my instructor to navigate directly to the evidence and documentation for any specific topic.

## 5. Difficulties faced
- While running commands inside restricted environments or sandboxes, initializing the `.git` directory directly had permission constraints on macOS until proper working directory access was confirmed.
- Ensuring the repository naming followed the exact requirement (`digital-detective-XXXX` with lowercase letters and hyphens, matching the folder name).

## 6. How I resolved them
- Confirmed directory permissions and ensured Git initialized cleanly on the `main` branch.
- Used the exact four digits `8430` to match the local directory name `digital-detective-8430`.

## 7. Evidence / files
- Project root: `README.md`
- Mission documentation: `mission-00-setup/README.md`
- Tool check outputs:
  ```text
  $ python3 --version
  Python 3.14.7

  $ git --version
  git version 2.54.0 (Apple Git-157)

  $ brew --version
  Homebrew 7.0.13
  ```

## 8. Commit details
- **Commit hash:** `ea370e4`
- **Commit message:** `Set up Digital Detective mission structure`
- **Target branch:** `main`
- **Remote status:** Committed locally; ready to push once GitHub remote is linked.
