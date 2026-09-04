"""Flask Team Directory — Git workshop demo app."""

from flask import Flask, render_template

from data import COMPANY_NAME, EMPLOYEES

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        company_name=COMPANY_NAME,
        employees=EMPLOYEES,
    )


if __name__ == "__main__":
    app.run(debug=True)
