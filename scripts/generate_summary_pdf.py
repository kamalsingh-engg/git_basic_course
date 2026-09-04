"""Generate WORKSHOP_SESSION_SUMMARY.pdf from session notes."""

from pathlib import Path

from fpdf import FPDF

ARTIFACTS = Path(__file__).resolve().parent.parent / "artifacts"
OUTPUT = ARTIFACTS / "WORKSHOP_SESSION_SUMMARY.pdf"

SECTIONS = [
    ("Git Basics Workshop - Session Summary", "title"),
    ("", "gap"),
    ("Student: kamalsingh-engg", "body"),
    ("Repository: github.com/kamalsingh-engg/git_basic_course", "body"),
    ("Project: Flask Team Directory (dummy employee data)", "body"),
    ("Date: September 4, 2026 | Duration: ~3 hours (Blocks 1-9)", "body"),
    ("", "gap"),
    ("1. PROJECT OVERVIEW", "heading"),
    (
        "We built a Flask web app showing 5 dummy employees. It was used to "
        "practice Git and GitHub end-to-end.",
        "body",
    ),
    ("Key files: app.py, data.py, templates/, static/style.css", "body"),
    (".github/workflows/ci.yml - GitHub Actions CI", "body"),
    ("WORKSHOP.md + artifacts/ - guides and cheat sheets", "body"),
    ("", "gap"),
    ("2. BLOCKS COMPLETED", "heading"),
    ("Block 1 - Setup & first commit (git init, add, commit)", "bullet"),
    ("Block 2 - GitHub remote, push, pull", "bullet"),
    ("Block 3 - Branching (feature/add-role-badge)", "bullet"),
    ("Block 4 - Pull Request #1 merged (role badges)", "bullet"),
    ("Block 5 - Pull Request #2 merged (footer)", "bullet"),
    ("Block 6 - Merge conflict in data.py (COMPANY_NAME)", "bullet"),
    ("Block 7 - checkout, switch, detached HEAD, restore", "bullet"),
    ("Block 8 - reset, revert, go back to previous commit", "bullet"),
    ("Block 9 - GitHub Actions CI + Pull Request #3 merged", "bullet"),
    ("", "gap"),
    ("3. FINAL COMMIT HISTORY", "heading"),
    ("8fa5095 - Merge PR #3 (GitHub Actions + extended docs)", "mono"),
    ("3f14990 - Resolve company name conflict", "mono"),
    ("5d33a90 - Merge PR #2 (footer)", "mono"),
    ("9336b9c - Merge PR #1 (role badges)", "mono"),
    ("f1573ac - Initial commit", "mono"),
    ("", "gap"),
    ("4. GIT COMMANDS LEARNED", "heading"),
    ("git init, status, add, commit, log", "bullet"),
    ("git remote, push, pull", "bullet"),
    ("git switch, branch, merge", "bullet"),
    ("git restore, restore --source=HASH", "bullet"),
    ("git switch --detach HASH (detached HEAD)", "bullet"),
    ("git reset --soft HEAD~1 (local undo)", "bullet"),
    ("git revert HASH (safe undo on shared branches)", "bullet"),
    ("git stash / git stash pop", "bullet"),
    ("", "gap"),
    ("5. GITHUB CONCEPTS", "heading"),
    ("Remote (origin) - GitHub copy of repo", "bullet"),
    ("Pull Request - review before merging to main", "bullet"),
    ("Branch protection - require PR for main", "bullet"),
    ("GitHub Actions - auto-test on every PR", "bullet"),
    ("Merge conflict - same line edited on two branches", "bullet"),
    ("", "gap"),
    ("6. STANDARD WORKFLOW", "heading"),
    ("feature branch -> add -> commit -> push -> open PR", "body"),
    ("CI runs (green check) -> merge PR -> git pull on main", "body"),
    ("", "gap"),
    ("7. WHEN TO USE WHAT", "heading"),
    ("Wrong file only -> git restore --source=HASH file", "bullet"),
    ("Undo local commit -> git reset --soft HEAD~1", "bullet"),
    ("Undo pushed commit -> git revert HASH (via PR)", "bullet"),
    ("Team merge to main -> always Pull Request", "bullet"),
    ("Auto-test on PR -> GitHub Actions (.github/workflows/ci.yml)", "bullet"),
    ("", "gap"),
    ("8. SUCCESS CRITERIA - ALL MET", "heading"),
    ("Flask app runs | 3 PRs merged | conflict resolved", "bullet"),
    ("checkout/restore practiced | reset/revert understood", "bullet"),
    ("GitHub Actions CI enabled and passing on main", "bullet"),
    ("", "gap"),
    ("Repo: https://github.com/kamalsingh-engg/git_basic_course", "body"),
    ("Generated from Cursor AI-guided Git Basics Workshop.", "footer"),
]


class SummaryPDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def build_pdf() -> None:
    pdf = SummaryPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    for text, kind in SECTIONS:
        if kind == "gap" or not text.strip():
            pdf.ln(4)
            continue
        if kind == "title":
            pdf.set_font("Helvetica", "B", 18)
            pdf.set_text_color(15, 33, 62)
            pdf.multi_cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
        elif kind == "heading":
            pdf.set_font("Helvetica", "B", 13)
            pdf.set_text_color(15, 52, 96)
            pdf.multi_cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)
        elif kind == "bullet":
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(30, 30, 30)
            pdf.multi_cell(0, 6, f"  -  {text}", new_x="LMARGIN", new_y="NEXT")
        elif kind == "mono":
            pdf.set_font("Courier", "", 9)
            pdf.set_text_color(50, 50, 50)
            pdf.multi_cell(0, 6, f"  {text}", new_x="LMARGIN", new_y="NEXT")
        elif kind == "footer":
            pdf.ln(6)
            pdf.set_font("Helvetica", "I", 9)
            pdf.set_text_color(100, 100, 100)
            pdf.multi_cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")
        else:
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(30, 30, 30)
            pdf.multi_cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUTPUT))
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
