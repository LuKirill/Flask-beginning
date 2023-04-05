from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from blog.creation.views import creation
from blog.user.views import user
from blog.auth.views import auth


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ')c46i=c^-in+6v4^%cw$m11m5ubaz(3vob1ffcdysa5+t@+tdj'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from blog.models import User

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(creation)
    app.register_blueprint(auth)

