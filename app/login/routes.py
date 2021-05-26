from flask import Blueprint
from .controllers import (UserLogin) #, AlunoLogin, ProfessorLogin

login_api = Blueprint('login_api', __name__)

login_api.add_url_rule(
    '/login', view_func= UserLogin.as_view('login_details'), methods = ['GET', 'POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)
'''
login_api.add_url_rule(
    '/aluno/login', view_func= AlunoLogin.as_view('aluno_login'), methods = ['POST']
)

login_api.add_url_rule(
    '/professor/login', view_func= ProfessorLogin.as_view('professor_login'), methods = ['POST']
)
'''