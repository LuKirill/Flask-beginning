from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

paper = Blueprint('paper', __name__, url_prefix='/papers', static_folder='../static')

PAPERS = {
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


@paper.route('/')
def paper_list():
    return render_template('papers/list.html', paper=PAPERS)


@paper.route('/<int:pk>')
def get_paper(pk: int):
    try:
        paper_name = PAPERS[pk]
    except KeyError:
        raise NotFound(f'Paper id {pk} not found')
    return render_template(
        'papers/details.html',
        apaper_name=paper_name,
    )