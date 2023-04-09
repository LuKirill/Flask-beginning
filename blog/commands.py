import click
from werkzeug.security import generate_password_hash

from blog.models.database import db


@click.command("init-db")
def init_db():
    from wsgi import app

    """
    Run in your terminal:
    flask init-db
    """

    from blog.models.user import User 
    db.create_all()
    print("done!")


@click.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User
    admin = User(username='admin', is_staff=True)
    user = User(username='user')

    db.session.add(admin)
    db.session.add(user)
    db.session.commit()

    print("done! created users:", admin, user)