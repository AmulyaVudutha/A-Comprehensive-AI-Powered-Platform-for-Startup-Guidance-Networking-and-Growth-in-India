from flask import Blueprint, request, render_template
from db import get_db_connection

startup_bp = Blueprint("startup", __name__)

@startup_bp.route("/startup", methods=["GET","POST"])
def startup():
    if request.method == "POST":
        data = (
            request.form["name"],
            request.form["domain"],
            request.form["stage"],
            request.form["funding"],
            request.form["team"],
            request.form["location"]
        )

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO startups
            (startup_name,domain,stage,funding_required,team_size,location)
            VALUES (%s,%s,%s,%s,%s,%s)""",
            data
        )
        conn.commit()
        conn.close()

        return "Startup Profile Saved"

    return render_template("startup_form.html")
