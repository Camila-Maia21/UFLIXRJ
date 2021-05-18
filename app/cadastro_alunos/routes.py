from flask import Blueprint
from app.cadastro_alunos.controllers import (AlunoDetails)

aluno_api = Blueprint('aluno_api', __name__,template_folder='template')

aluno_api.add_url_rule(
    '/aluno', view_func = AlunoDetails.as_view('aluno_details'), methods = ['GET', 'POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)
'''
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)
'''