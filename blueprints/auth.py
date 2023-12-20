from flask import Blueprint, render_template, jsonify
from exts import mail, db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCapcthaModel

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login")
def login_page():
    pass


@bp.route("/register")
def register_page():
    return render_template("register.html")


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
                      body="你好郑先生，什么时候有时间，我们去滑冰呀。")
    mail.send(message)
    return "sent successfully"
