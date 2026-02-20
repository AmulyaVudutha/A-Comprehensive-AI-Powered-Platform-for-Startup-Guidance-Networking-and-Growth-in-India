from flask import Blueprint, request, render_template, redirect, url_for
from db import get_db_connection
import hashlib

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        role = request.form["role"]
        password = hashlib.sha256(request.form["password"].encode()).hexdigest()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name,email,password,role) VALUES (%s,%s,%s,%s)",
            (name,email,password,role)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = hashlib.sha256(request.form["password"].encode()).hexdigest()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email,password)
        )
        user = cur.fetchone()
        conn.close()

        if user:
            return redirect("/dashboard")

    return render_template("login.html")
