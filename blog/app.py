from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from blog.creation.views import creation
from blog.user.views import user
from blog.auth.views import auth
from blog.models.database import db
from blog import commands

import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = ')c46i=c^-in+6v4^%cw$m11m5ubaz(3vob1ffcdysa5+t@+tdj'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

    db.init_app(app)
    Migrate(app, db)

    cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from blog.models import User

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))
    register_commands(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(creation)
    app.register_blueprint(auth)

def register_commands(app):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
