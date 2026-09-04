# 2-Hour Git Basics Workshop — Hands-On Guide

Follow this guide step by step. Read `artifacts/PROCESS_FLOW.md` for the visual timeline.

**Replace `YOUR_GITHUB_USERNAME`** with your real GitHub username before connecting the remote.

---

## Part 0 — Verify environment (5 min)

```powershell
cd d:\skill\basics_of_git
python --version
git --version
```

---

## Part 1 — Run Flask app (10 min)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Visit http://127.0.0.1:5000 — Team Directory with 5 dummy employees.

Stop the server with `Ctrl+C` when done.

---

## Part 2 — First commit (15 min)

```powershell
git init
git add .
git commit -m "Initial commit: Flask team directory with dummy data"
```

**Exercise:** Run `git status`, `git log --oneline`, and `git show HEAD`.

---

## Part 3 — GitHub + push + pull (20 min)

1. Create repo on GitHub (empty, no README).
2. Run:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/git-basics-workshop.git
git push -u origin main
```

3. Refresh GitHub — files should appear.
4. Run `git pull origin main` (should say "Already up to date").

---

## Part 4 — Feature branch + PR (25 min)

### Step A — Role badge feature

```powershell
git switch -c feature/add-role-badge
```

Edit `templates/index.html`: inside the employee card loop, add after the name:

```html
<span class="badge">{{ employee.role }}</span>
```

Commit and push:

```powershell
git add templates/index.html
git commit -m "Add role badge to employee cards"
git push -u origin feature/add-role-badge
```

### Step B — Open Pull Request

On GitHub: **Compare & pull request** → merge into `main` → **Merge pull request**.

### Step C — Update local main

```powershell
git switch main
git pull origin main
python app.py
```

Confirm role badges appear.

---

## Part 5 — Second feature: footer (20 min)

```powershell
git switch -c feature/add-footer
```

Edit `templates/base.html` — add before `</body>`:

```html
<footer class="site-footer">
  <p>Team Directory &copy; 2026 — Git Workshop Demo</p>
</footer>
```

Add to `static/style.css`:

```css
.site-footer {
  text-align: center;
  padding: 1rem;
  color: #666;
  margin-top: 2rem;
}
```

```powershell
git add templates/base.html static/style.css
git commit -m "Add copyright footer to all pages"
git push -u origin feature/add-footer
```

Open PR #2 on GitHub, merge, then:

```powershell
git switch main
git pull origin main
```

---

## Part 6 — Merge conflict drill (25 min)

We will create a conflict on `data.py` field `COMPANY_NAME`.

### Branch 1 (merge first)

```powershell
git switch main
git switch -c branch/update-company-name
```

Open `data.py`, change:

```python
COMPANY_NAME = "Acme Corp"
```

to:

```python
COMPANY_NAME = "Acme Corporation"
```

```powershell
git add data.py
git commit -m "Expand company name to Acme Corporation"
git switch main
git merge branch/update-company-name
```

### Branch 2 (conflict)

```powershell
git switch -c branch/short-company-name
```

Change the **same line** in `data.py` to:

```python
COMPANY_NAME = "Acme Co."
```

```powershell
git add data.py
git commit -m "Shorten company name to Acme Co."
git switch main
git merge branch/short-company-name
```

Git will report a **merge conflict**. Open `data.py`, fix markers, pick one name (or combine), then:

```powershell
git add data.py
git commit -m "Resolve company name conflict — keep Acme Corporation"
git push origin main
```

---

## Part 7 — Wrap-up (5 min)

Run:

```powershell
git log --oneline --graph --all -15
git branch -a
```

**Quiz yourself:**

1. What is the difference between `git add` and `git commit`?
2. Why use a branch before opening a PR?
3. What does `git pull` do after someone merges your PR on GitHub?
4. What do `<<<<<<<` lines mean?

---

## Optional stretch goals

- Add `feature/employee-count` — show total employees in header
- Use `git stash` before switching branches with dirty working tree
- Tag a release: `git tag v1.0.0` and `git push origin v1.0.0`
