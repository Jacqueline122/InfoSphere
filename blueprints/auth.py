from flask import Blueprint, render_template

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login_page():
    pass


@bp.route("/register")
def register_page():
    return render_template("register.html")