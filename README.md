# Git Basics Workshop — Flask Team Directory

A hands-on workshop to practice Git and GitHub with a minimal Flask app that displays dummy employee data.

**Core path:** ~2 hours (Blocks 1–6)  
**Extended path:** ~3+ hours (adds checkout, undo commits, GitHub Actions)

## Quick start

```powershell
cd d:\skill\basics_of_git
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Workshop materials

| File | Purpose |
|------|---------|
| [WORKSHOP.md](WORKSHOP.md) | Step-by-step hands-on guide (start here) |
| [artifacts/PROCESS_FLOW.md](artifacts/PROCESS_FLOW.md) | Timeline + mermaid diagrams (Blocks 1–9) |
| [artifacts/GIT_CHEATSHEET.md](artifacts/GIT_CHEATSHEET.md) | Command reference |

## GitHub setup

Repo: https://github.com/kamalsingh-engg/git_basic_course

```powershell
git init
git add .
git commit -m "Initial commit: Flask team directory with dummy data"
git branch -M main
git remote add origin https://github.com/kamalsingh-engg/git_basic_course.git
git push -u origin main
```

## What you will practice

### Core (Blocks 1–6)

- `git init`, `add`, `commit`, `status`, `log`
- `remote`, `push`, `pull`
- Branches: `switch`, `merge`
- Pull Requests on GitHub
- Resolving a merge conflict in `data.py`

### Extended (Blocks 7–9)

- **`checkout` / `switch`** — move between branches, detached HEAD
- **Go back to a previous commit** — `restore`, `reset`, `revert`
- **GitHub Actions** — automated CI tests on every PR
- **Branch protection** — require PR before merging to `main`

## Branch policy (recommended)

All changes to `main` should go through a **Pull Request**. Enable on GitHub:

**Settings → Branches → Add rule for `main`**

- Require a pull request before merging
- Require status checks to pass (after enabling GitHub Actions)

## GitHub Actions

CI workflow: `.github/workflows/ci.yml`

Runs on push to `main` and on every Pull Request. It installs Python, installs dependencies, and smoke-tests the Flask homepage.

```powershell
git switch -c feature/add-github-actions
git add .github/workflows/ci.yml
git commit -m "Add GitHub Actions CI workflow"
git push -u origin feature/add-github-actions
```

Open a PR → check the **Actions** tab for a green check.

## Project structure

```
basics_of_git/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI
├── app.py                  # Flask routes
├── data.py                 # Dummy employee data
├── templates/              # HTML templates
├── static/style.css        # Styles
├── artifacts/              # Workshop docs
├── WORKSHOP.md
└── requirements.txt
```

## Topic map

| Topic | Block | Key commands |
|-------|-------|--------------|
| First commit | 1 | `add`, `commit` |
| Push / pull | 2 | `push`, `pull`, `remote` |
| Branching | 3 | `switch`, `branch` |
| Pull Request | 4–5 | PR on GitHub |
| Merge conflict | 6 | `merge`, resolve markers |
| Checkout | 7 | `switch`, `checkout`, `--detach` |
| Undo commits | 8 | `restore`, `reset`, `revert` |
| GitHub Actions | 9 | `.github/workflows/ci.yml` |
