from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

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