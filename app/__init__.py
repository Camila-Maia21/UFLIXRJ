from flask import Flask 

from app.cadastro_alunos.model import Alunos
from app.cadastro_professores.model import Professores
from app.cadastro_alunos.controllers import cadastro, cadastroalunos
from app.cadastro_professores.controllers import cadastro, cadastroprofessores



def create_app():
    app = Flask(__name__)

    app.cadastroA(app)
    app.cadastroP(app)
    app.cadastroalunos(app)
    app.cadastroprofessores(app)

    return app