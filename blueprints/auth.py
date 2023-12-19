from flask import Blueprint, render_template
from exts import mail
from flask_mail import Message
from flask import request
import string
import random

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
    source = string.digits*4
    captcha = random.sample(source, 4)
    print(captcha)
    captcha = "".join(captcha)
    message = Message(subject="InforSphere register verification code", recipients=[email], body=f"Your verification code is:{captcha} ")
    mail.send(message)
    
    return "success"




@bp.route("/mail/test")
def mail_test():
    message = Message(subject="email test", recipients=["long_j1@denison.edu"], body="This is test")
    mail.send(message)
    return "sent successfully"
