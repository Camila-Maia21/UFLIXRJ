from flask import Blueprint
from app.cadastro_alunos.controllers import (AlunoCreate, AlunoDetails)

aluno_api = Blueprint('aluno_api', __name__,template_folder='template')

aluno_api.add_url_rule(
    '/aluno', view_func = AlunoCreate.as_view('aluno_create'), methods = ['GET', 'POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)
aluno_api.add_url_rule(
    '/aluno/<int:id>', view_func = AlunoDetails.as_view('aluno_details'), methods = ['GET', 'PUT', 'PATCH', 'DELETE']
)
