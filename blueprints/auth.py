from flask import Blueprint

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login_page():
    pass
