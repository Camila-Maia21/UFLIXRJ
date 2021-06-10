from flask import Blueprint
from app.cadastro.controllers import (AlunoCreate, ProfessorCreate, UserDetails)

user_api = Blueprint('user_api', __name__,template_folder='template')

user_api.add_url_rule(
    '/cadastroaluno', view_func = AlunoCreate.as_view('aluno_create'), methods = ['GET', 'POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)
user_api.add_url_rule(
    '/user/<int:id>', view_func = UserDetails.as_view('user_details'), methods = ['GET', 'PUT', 'PATCH', 'DELETE']
)
user_api.add_url_rule(
    '/cadastroprofessor', view_func = ProfessorCreate.as_view('professor_create'), methods = ['GET', 'POST']
)

