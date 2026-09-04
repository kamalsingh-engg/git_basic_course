# Git Basics Workshop — Flask Team Directory

A **2-hour hands-on workshop** to practice Git and GitHub with a minimal Flask app that displays dummy employee data.

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
| [WORKSHOP.md](WORKSHOP.md) | Step-by-step 2-hour guide (start here) |
| [artifacts/PROCESS_FLOW.md](artifacts/PROCESS_FLOW.md) | Timeline + mermaid diagrams |
| [artifacts/GIT_CHEATSHEET.md](artifacts/GIT_CHEATSHEET.md) | Command reference |

## GitHub setup

1. Create an empty repo on GitHub (e.g. `git-basics-workshop`).
2. Replace `YOUR_GITHUB_USERNAME` in the workshop docs with your username.
3. Follow **Part 3** in [WORKSHOP.md](WORKSHOP.md) to connect and push.

```powershell
git init
git add .
git commit -m "Initial commit: Flask team directory with dummy data"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/git-basics-workshop.git
git push -u origin main
```

## What you will practice

- `git init`, `add`, `commit`, `status`, `log`
- `remote`, `push`, `pull`
- Branches: `switch`, `merge`
- Pull Requests on GitHub
- Resolving a merge conflict in `data.py`

## Project structure

```
basics_of_git/
├── app.py              # Flask routes
├── data.py             # Dummy employee data
├── templates/          # HTML templates
├── static/style.css    # Styles
├── artifacts/          # Workshop docs
├── WORKSHOP.md         # Main guide
└── requirements.txt
```
