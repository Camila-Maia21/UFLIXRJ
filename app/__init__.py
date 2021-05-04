from flask import Flask 

from app.cadastro_alunos.model import Alunos
from app.cadastro_professores.model import Professores
from app.cadastro_alunos.controllers import alunos_api
from app.cadastro_professores.controllers import professores_api


def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(professores_api)
    app.register_blueprint(alunos_api)


    return app