from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from flask_login import current_user

from blog.database import db
from blog.forms.article import CreateArticleForm
from blog.mymodels import Article, Author

creation = Blueprint('creation', __name__, url_prefix='/creation', static_folder='../static')

CREATIONS = {
    1: {
        'title': 'Ruslan and Ludmila',
        'text': '1 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin mollis urna eu malesuada commodo. Suspendisse lacinia, velit vitae mattis ',
        'author': 1,
    },
    2: {
        'title': 'Borodino',
        'text': '2 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin mollis urna eu malesuada commodo. Suspendisse lacinia, velit vitae mattis ',
        'author': 2,
    },
    3: {
        'title': 'War and Peace',
        'text': '3 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin mollis urna eu malesuada commodo. Suspendisse lacinia, velit vitae mattis ',
        'author': 3,
    }
}


@creation.route('/')
def creation_list():
    return render_template('creations/list.html', creation=CREATIONS)


@creation.route('/<int:pk>')
def get_creation(pk: int):
    try:
        creation_name = CREATIONS[pk]
    except KeyError:
        raise NotFound(f'Creation id {pk} not found')
    return render_template(
        'creations/details.html',
        creation_name=creation_name,
    )

@article.route('/create/', methods=['GET'])
def create_article_form():
    form = CreateArticleForm(request.form)
    return render_template('articles/create.html', form=form)


@article.route('/', methods=['POST'])
def create_article():
    form = CreateArticleForm(request.form)
    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)
        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.article_detail', article_id=_article.id))

    return render_template('articles/create.html', form=form)