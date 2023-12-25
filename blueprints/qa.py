from flask import Blueprint, request, render_template, g, redirect, url_for
from .forms import QuestionForm
from models import QuestionModel
from exts import db
from decorators import login_required

# /auth
bp = Blueprint("qa", __name__, url_prefix="/")


# http://127.0.0.1:5000
@bp.route("/")
def index():
    return "Home Page"


@bp.route("/qa/public", methods=['GET', 'POST'])
@login_required
def public_question():
    if request.method == "GET":
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for("qa.public_question"))
