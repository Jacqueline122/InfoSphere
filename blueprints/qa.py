from flask import Blueprint

# /auth
bp = Blueprint("qa", __name__, url_prefix="/")


# http://127.0.0.1:5000
@bp.route("/")
def index():
    return "Home Page"
