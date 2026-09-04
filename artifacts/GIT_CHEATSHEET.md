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
git switch -c feature/x       # Create + switch
git switch main               # Back to main
git merge feature/x           # Merge branch into current
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
4. Review → **Merge pull request**
5. Locally: `git switch main` then `git pull`

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

## Useful Extras

```powershell
git log --oneline --graph --all -10
git diff                      # Unstaged changes
git diff --staged             # Staged changes
git restore <file>            # Discard unstaged changes
git show <commit-hash>        # View one commit
```

## Good Commit Messages

- **Do:** `Add department column to team table`
- **Don't:** `fix`, `update`, `changes`

Use imperative mood: "Add", "Fix", "Remove", not "Added" or "Adding".
