from flask import Blueprint
from app.cadastro_alunos.controllers import (AlunoDetails)

aluno_api = Blueprint('aluno_api', __name__)

aluno_api.add_url_rule(
    '/aluno', view_func = AlunoDetails.as_view('aluno_details'), methods = ['GET', 'POST']
)