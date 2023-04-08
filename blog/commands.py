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

    db.session.add(
        User(email='name@email.com', password=generate_password_hash('123'))
    )
    db.session.commit()