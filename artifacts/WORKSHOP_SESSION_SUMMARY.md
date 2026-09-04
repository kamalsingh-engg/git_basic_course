# Git Basics Workshop — Session Summary

**Student:** kamalsingh-engg  
**Repository:** https://github.com/kamalsingh-engg/git_basic_course  
**Project:** Flask Team Directory (dummy employee data)  
**Date:** September 4, 2026  
**Duration:** ~3 hours (Blocks 1–9)

---

## 1. Project Overview

We built a simple **Flask web application** that displays a Team Directory with 5 dummy employees. The app was used as a hands-on vehicle to learn Git and GitHub workflows.

| File | Purpose |
|------|---------|
| `app.py` | Flask routes |
| `data.py` | Dummy employee data (`COMPANY_NAME`, `EMPLOYEES`) |
| `templates/` | HTML pages (base layout + index) |
| `static/style.css` | Styling |
| `.github/workflows/ci.yml` | GitHub Actions CI (automated tests) |
| `WORKSHOP.md` | Step-by-step guide |
| `artifacts/` | Process flow, cheat sheet, this summary |

**Run locally:**
```powershell
cd d:\skill\basics_of_git
.\venv\Scripts\Activate.ps1
python app.py
# Open http://127.0.0.1:5000
```

---

## 2. What We Completed (Block by Block)

### Block 1 — Setup & First Commit
- Created Flask app with dummy data
- Ran `git init`, `git add .`, `git commit`
- First commit: `f1573ac` — Initial commit

### Block 2 — GitHub Remote, Push & Pull
- Created GitHub repo: `git_basic_course`
- Connected remote: `https://github.com/kamalsingh-engg/git_basic_course.git`
- Pushed to `main` with `git push -u origin main`
- Practiced `git pull origin main`

### Block 3 — Branching
- Created branch: `feature/add-role-badge`
- Added role badge next to employee names in `templates/index.html`
- Committed and pushed feature branch

### Block 4 — Pull Request #1
- Opened PR on GitHub: feature → main
- Self-reviewed changes on GitHub
- Merged PR #1: **Add role badge to employee cards**
- Synced local main: `git switch main` → `git pull`

### Block 5 — Second Feature + PR #2
- Branch: `feature/add-footer`
- Added copyright footer to `templates/base.html` + CSS
- Opened and merged PR #2
- Pulled latest `main`

### Block 6 — Merge Conflict Drill
- Branch 1: changed `COMPANY_NAME` to `"Acme Corporation"` → merged cleanly
- Branch 2: changed same line to `"Acme Co."` → **CONFLICT**
- Resolved conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) in `data.py`
- Committed: `Resolve company name conflict — keep Acme Corporation`

**Lesson learned:** PRs are for team review on GitHub; `git merge` is the underlying Git operation. Block 6 used local merge to teach conflict resolution directly.

### Block 7 — Checkout & Switch
- Practiced `git switch` between branches
- Classic equivalent: `git checkout`
- **Detached HEAD:** `git switch --detach f1573ac` to view old code
- **Restore file from history:** `git restore --source=f1573ac data.py`
- Used `git stash` to temporarily save uncommitted work

### Block 8 — Go Back to Previous Commit
- **View history:** `git log`, `git show`
- **`git restore --source=HASH file`** — safe, one file only
- **`git reset --soft HEAD~1`** — undo local commit, keep changes staged
- **`git reset --hard`** — destructive, local only
- **`git revert HASH`** — safe undo on pushed/shared branches (creates new commit)

### Block 9 — GitHub Actions
- Added `.github/workflows/ci.yml`
- CI runs on every push to `main` and every Pull Request
- Smoke test: installs Python, Flask, checks homepage returns 200 + employee data
- Pushed via `feature/add-github-actions` branch
- Merged **PR #3** — CI + extended workshop docs (Blocks 7–9)

---

## 3. Final Commit History

```
8fa5095  Merge pull request #3 — GitHub Actions + extended docs
7d166f5  Add GitHub Actions CI and extended workshop docs (Blocks 7-9)
3f14990  Resolve company name conflict — keep Acme Corporation
5d33a90  Merge pull request #2 — footer
3a8b113  Add copyright footer to all pages
9336b9c  Merge pull request #1 — role badges
09f1851  Add role badge to employee cards
f1573ac  Initial commit — Flask team directory with dummy data
```

---

## 4. Git Commands Learned

| Command | What it does |
|---------|--------------|
| `git init` | Start a new Git repository |
| `git status` | Show changed / staged files |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Save a snapshot |
| `git log --oneline --graph` | View history |
| `git remote add origin URL` | Link GitHub repo |
| `git push -u origin main` | Upload to GitHub |
| `git pull origin main` | Download + merge from GitHub |
| `git switch -c branch` | Create and switch branch |
| `git switch branch` | Switch branch |
| `git merge branch` | Merge branch into current |
| `git restore file` | Discard unstaged changes |
| `git restore --source=HASH file` | Get file from old commit |
| `git switch --detach HASH` | View repo at old commit |
| `git reset --soft HEAD~1` | Undo last commit (keep changes) |
| `git revert HASH` | Undo a pushed commit safely |
| `git stash` / `git stash pop` | Temporarily save work |

---

## 5. GitHub Concepts Learned

| Concept | Description |
|---------|-------------|
| **Remote** | GitHub copy of your repo (`origin`) |
| **Pull Request** | Propose changes; review before merging to `main` |
| **Merge** | Combine branch into `main` |
| **Branch protection** | Rule: all changes to `main` must go through a PR |
| **GitHub Actions** | Automated CI pipeline (tests on every PR) |
| **Merge conflict** | Same line edited on two branches — manual fix required |

---

## 6. Workflow Diagram

```
Edit code on feature branch
        ↓
git add → git commit
        ↓
git push origin feature-branch
        ↓
Open Pull Request on GitHub
        ↓
CI runs (GitHub Actions) ✓
        ↓
Merge Pull Request
        ↓
git switch main → git pull
```

---

## 7. Branch Policy (Recommended)

On GitHub **Settings → Branches → Rule for `main`:**
- Require a pull request before merging
- Require status checks to pass (CI)

This prevents direct `git push origin main` and enforces team-style workflow.

---

## 8. Success Criteria — All Met

- [x] Flask app runs with dummy team data
- [x] Multiple commits on `main`
- [x] Feature branches created and pushed
- [x] 3 Pull Requests merged on GitHub
- [x] `git pull` used after each merge
- [x] Merge conflict resolved in `data.py`
- [x] Checkout, detached HEAD, restore practiced
- [x] `reset` and `revert` understood
- [x] GitHub Actions CI enabled and passing
- [x] Extended docs added (Blocks 7–9)

---

## 9. Quick Reference — When to Use What

| Situation | Command |
|-----------|---------|
| Save work | `git add` + `git commit` |
| Upload branch | `git push` |
| Get latest main | `git pull` |
| New feature | `git switch -c feature/name` |
| Merge to main (team) | Pull Request on GitHub |
| Wrong file only | `git restore --source=HASH file` |
| Undo local commit | `git reset --soft HEAD~1` |
| Undo pushed commit | `git revert HASH` → PR |
| View old code | `git switch --detach HASH` |

---

## 10. Repository Links

- **Repo:** https://github.com/kamalsingh-engg/git_basic_course
- **Actions:** https://github.com/kamalsingh-engg/git_basic_course/actions
- **Pull Requests:** https://github.com/kamalsingh-engg/git_basic_course/pulls

---

*Generated from the Cursor AI–guided Git Basics Workshop session.*
