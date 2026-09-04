# Git Cheat Sheet — Workshop Edition

## The Three Trees

```
Working Directory  →  Staging (index)  →  Repository (.git)
     (edit)              git add              git commit
```

## Daily Workflow

```powershell
git status                    # What changed?
git add .                     # Stage changes
git commit -m "Describe why"  # Save snapshot
git push                      # Send to GitHub
git pull                      # Get from GitHub
```

## Branches

```powershell
git branch                    # List branches
git switch -c feature/x       # Create + switch (modern)
git switch main               # Switch to existing branch
git merge feature/x           # Merge branch into current
```

## Checkout vs Switch

`checkout` is the **classic** command; Git now splits it into clearer commands:

| Goal | Modern (Git 2.23+) | Classic |
|------|--------------------|---------|
| Switch branch | `git switch main` | `git checkout main` |
| Create branch | `git switch -c feature/x` | `git checkout -b feature/x` |
| Restore a file | `git restore file` | `git checkout -- file` |
| File from old commit | `git restore --source=HASH file` | `git checkout HASH -- file` |

```powershell
git switch feature/add-footer     # go to branch
git switch -c feature/new-thing   # create + go
git switch --detach abc1234       # view repo at commit (detached HEAD)
git switch main                   # return to branch
```

### Detached HEAD

When you `git switch --detach <hash>`, you are not on a branch — just viewing history.

```powershell
git log --oneline -5
git switch --detach f1573ac       # look around
git switch main                   # always come back before new commits
```

## Go Back to a Previous Commit

### View history

```powershell
git log --oneline --graph --all -15
git log --oneline data.py         # history for one file
git show abc1234                  # one commit's diff
```

### Restore one file from history (safe)

```powershell
git restore --source=HEAD~1 templates/index.html   # previous commit
git restore --source=f1573ac data.py                 # specific commit
git restore templates/index.html                     # discard that change
```

### `git reset` — move branch back (local, use carefully)

```powershell
git reset --soft HEAD~1       # undo commit, keep changes staged
git reset HEAD~1              # undo commit, keep changes unstaged (mixed)
git reset --hard HEAD~1       # undo commit AND discard changes (destructive)
```

| Command | Moves branch? | Keeps file changes? |
|---------|---------------|---------------------|
| `--soft` | Yes | Yes, staged |
| `--mixed` | Yes | Yes, unstaged |
| `--hard` | Yes | **No — deleted** |

> **Rule:** If already pushed to GitHub → use `git revert`, not `reset --hard`.

### `git revert` — undo on shared branches (safe)

Creates a new commit that reverses an old one:

```powershell
git revert HEAD                 # undo last commit
git revert abc1234 --no-edit    # undo specific commit
git push origin main            # share the revert (via PR in real projects)
```

## Remote

```powershell
git remote add origin <URL>
git push -u origin main       # First push sets upstream
git push                      # Later pushes
git pull origin main
```

## Pull Request (on GitHub website)

1. Push a branch: `git push -u origin my-branch`
2. GitHub → **Pull requests** → **New**
3. Base: `main`, Compare: `my-branch`
4. Review → wait for **CI check** (if Actions enabled)
5. **Merge pull request**
6. Locally: `git switch main` then `git pull`

## Branch protection (GitHub Settings)

Require PR before merging to `main`:

- **Settings → Branches → Add rule**
- Branch: `main`
- ✅ Require a pull request before merging
- ✅ Require status checks to pass (optional — needs GitHub Actions)

## Merge Conflict Markers

```
<<<<<<< HEAD
code from current branch
=======
code from incoming branch
>>>>>>> branch-name
```

**Fix:** Edit file to keep the correct text, delete all marker lines, then:

```powershell
git add <file>
git commit -m "Resolve merge conflict in <file>"
```

## GitHub Actions (CI)

Workflow file: `.github/workflows/ci.yml`

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

| Term | Meaning |
|------|---------|
| **Workflow** | Automated pipeline (YAML file) |
| **Job** | Group of steps (e.g. `test`) |
| **Step** | One command (install, test, deploy) |
| **Runner** | Virtual machine that runs the job |

```powershell
# After adding workflow file:
git add .github/workflows/ci.yml
git commit -m "Add GitHub Actions CI"
git push -u origin feature/add-ci
# Open PR → Actions tab shows green ✓ or red ✗
```

View runs: GitHub repo → **Actions** tab.

## Useful Extras

```powershell
git log --oneline --graph --all -10
git diff                      # Unstaged changes
git diff --staged             # Staged changes
git restore <file>            # Discard unstaged changes
git show <commit-hash>        # View one commit
git stash                     # Temporarily save uncommitted work
git stash pop                 # Restore stashed work
```

## Good Commit Messages

- **Do:** `Add department column to team table`
- **Don't:** `fix`, `update`, `changes`

Use imperative mood: "Add", "Fix", "Remove", not "Added" or "Adding".

## Quick decision guide

```
Wrong file only?        → git restore --source=HASH file
Undo local commit?      → git reset --soft HEAD~1
Undo pushed commit?     → git revert HASH (then PR)
Switch branch?          → git switch branch-name
See old code?           → git switch --detach HASH
Team merge to main?     → Pull Request on GitHub
Auto-test on PR?        → GitHub Actions
```
