from flask import Blueprint, render_template, jsonify, redirect, url_for
from exts import mail, db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCapcthaModel, UserModel
from .forms import RegisterForm
from werkzeug.security import generate_password_hash

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login():
    return "login page"


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))


@bp.route("/captcha/email")
def captcha_email():
    email = request.args.get("email")
    source = string.digits * 4
    captcha = random.sample(source, 4)
    print(captcha)
    captcha = "".join(captcha)
    message = Message(subject="InforSphere register verification code", recipients=[email],
                      body=f"Your verification code is:{captcha} ")
    mail.send(message)
    email_captcha = EmailCapcthaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()

    return jsonify({"code": 200, "message": "", "data": None})


@bp.route("/mail/test")
def mail_test():
    message = Message(subject="email test", recipients=["gary313312849@gmail.com"],
                      body="something")
    mail.send(message)
    return "sent successfully"
