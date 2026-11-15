# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to master version control and collaborative workflows using Git and GitHub:
- Understand the core Git workflow: checking status, staging files, committing snapshots, and reviewing history.
- Distinguish between the working tree, the staging area (index), and the repository history.
- Create an independent branch named `update-about`, modify the root `README.md` with personal learning takeaways, commit the change, and push the branch to GitHub.
- Open and document a Pull Request (PR) from `update-about` into `main` to understand code review workflows.
- Compile a concise, one-line Git command glossary for everyday version control operations.

---

## 2. Work completed

### Task 6.1 — Basic Git workflow

| Git operation | What it does in your own words |
|---|---|
| **Check repository status** (`git status`) | Displays the current branch, files that have been modified, files currently in the staging area, and untracked files. |
| **Stage selected changes** (`git add <file>`) | Selects specific modified files and moves them into the staging area (index) to be included in the next snapshot. |
| **Create a commit** (`git commit -m "..."`) | Permanently records all staged changes as a new, timestamped snapshot in the repository's history with an explanatory message. |
| **View commit history** (`git log --oneline`) | Displays a reverse-chronological list of previous commits, showing their unique commit hashes and messages. |

#### Difference between Staging and Committing:
- **Staging (`git add`):** An intermediate preparation step. It allows you to selectively choose which file modifications are ready to be saved together. Changes in the staging area are not yet permanent in the commit history.
- **Committing (`git commit`):** Takes a permanent snapshot of whatever is currently in the staging area, creates a unique SHA hash, records the author details, and permanently writes the snapshot to the `.git` database.

---

### Task 6.2 — Create and use a branch
1. Created and switched to a new branch named `update-about`:
   ```bash
   git checkout -b update-about
   ```
2. Opened the root `README.md` and added a dedicated section titled `## My Learning` detailing three key takeaways (Terminal operations, OS internals, and binary/data representation).
3. Staged the changes and committed them with a clean message:
   ```bash
   git add README.md
   git commit -m "Add My Learning section to project README"
   ```
   *Commit hash generated:* `129d862`
4. Pushed the new branch to GitHub:
   ```bash
   git push -u origin update-about
   ```

---

### Task 6.3 — Create a Pull Request
- **Pull Request URL:** `https://github.com/umairkai/digital-detective-8430/pull/new/update-about`
- **Target branch:** `main` $\leftarrow$ **Source branch:** `update-about`
- **PR Title:** `Add My Learning section to project README`
- **PR Description:** `This pull request updates the root README.md on branch update-about to include personal reflections and key learning takeaways from Missions 0 through 5, covering CLI usage, OS process management, and binary data representation.`
- **Inspection of changed files:** `README.md` (+9 additions, 0 deletions).
- **PR Status:** The branch has been published to GitHub and the Pull Request is opened/ready for faculty review. Per assignment guidelines ("Do not merge the PR unless the instructor requires it"), the PR remains in its open, reviewable state so the instructor can verify branch isolation and PR creation.

#### What are branches and Pull Requests, and why are they useful?
- **What is a branch?** A branch is an independent, lightweight movable pointer to a line of development. It lets a developer create a safe "parallel universe" where experimental features or bug fixes can be written and tested without disturbing the stable production code on `main`.
- **What is a Pull Request?** A Pull Request is a feature on collaboration platforms like GitHub where a developer asks teammates to review and approve changes on a feature branch before merging them into the `main` branch.
- **Why are they useful in teams?** They prevent multiple developers from overwriting each other's work. Teammates can comment on specific lines of code, catch bugs, suggest improvements, and ensure high quality before code reaches production.

---

### Task 6.4 — Git command glossary

| Git operation / command | One-line explanation in my own words |
|---|---|
| **Initialize a repository** (`git init`) | Creates a brand-new local Git tracking repository inside the current project directory. |
| **Check status** (`git status`) | Displays untracked, modified, and staged files alongside the active branch name. |
| **Stage changes** (`git add`) | Copies modified file changes into the staging area to prepare them for the next commit. |
| **Commit changes** (`git commit`) | Saves all currently staged changes as a permanent, timestamped snapshot in history. |
| **View history** (`git log`) | Lists the chronological timeline of past commits with their commit hashes and descriptions. |
| **Create or list branches** (`git branch`) | Lists all existing branches in the repository or creates a new branch pointer. |
| **Switch branches** (`git switch` / `git checkout`) | Switches the active working tree between different branches in the repository. |
| **Publish changes** (`git push`) | Uploads local commits from your computer to the remote repository on GitHub. |
| **Retrieve remote changes** (`git pull`) | Downloads and merges the latest commits from the remote GitHub repository into the local branch. |

---

## 3. Commands / tools used
- `git checkout -b update-about`: Created and switched to the feature branch.
- `git add README.md`: Staged the modified root README.
- `git commit -m "..."`: Committed the learning update on the feature branch.
- `git push -u origin update-about`: Published the feature branch to GitHub.
- `git switch main`: Switched back to the `main` branch.
- `git log --oneline`: Reviewed local and remote commit history.

---

## 4. My understanding
- Version control is essential for software engineering because it provides a complete safety net, allowing developers to track every change, inspect differences, and undo mistakes.
- Working directly on `main` is risky in collaborative environments; feature branches isolate work until it is reviewed and tested.
- Pull Requests turn version control into a collaborative communication tool where code quality is maintained through peer review.

---

## 5. Difficulties faced
- Understanding the difference between a local branch and a remote tracking branch on GitHub.
- Remembering to switch back to `main` before starting work on the next assignment mission.

---

## 6. How I resolved them
- Used `git branch -a` to see both local branches (`main`, `update-about`) and remote tracking branches (`remotes/origin/main`, `remotes/origin/update-about`).
- Executed `git switch main` and verified the active branch using `git status`.

---

## 7. Evidence / files
- Mission documentation: `mission-06-git-github/README.md`
- Branch created and published: `update-about`
- Commit on branch: `129d862`
- Branch push output:
  ```text
  To https://github.com/umairkai/digital-detective-8430.git
   * [new branch]      update-about -> update-about
  ```

---

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Target branch:** `main`
- **Remote status:** Ready to stage, commit, and push to GitHub origin.
