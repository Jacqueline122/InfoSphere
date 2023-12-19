from flask import Flask
import config
from exts import db, mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate


app = Flask(__name__)
# Binding configuration file
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
