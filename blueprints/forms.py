import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailCapcthaModel
from exts import db


# Form: verify the code is corresponded or not
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="email format error")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="code format error")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="username format error")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="password format error")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="passwords must match")])

    # self design
    # 1. The email is registered or not
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="Email already registered")

    # 2. Verification code is correct or not
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCapcthaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="Email or verification code is invalid")
        # else:
        #     db.session.delete(captcha_model)
        #     db.session.commit()


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="email format error")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="password format error")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="title format error")])
    content = wtforms.StringField(validators=[Length(min=3, max=200, message="content format error")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, max=200, message="content format error")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="question id required")])
