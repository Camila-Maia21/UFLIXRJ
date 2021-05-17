from flask import Flask 
from app.extensions import db, migrate
from app.config import Config

from app.cadastro_alunos.routes import aluno_api
from app.cadastro_professores.routes import professor_api
from app.materia.routes import materia_api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(professor_api)
    app.register_blueprint(aluno_api)
    app.register_blueprint(materia_api)


    return app