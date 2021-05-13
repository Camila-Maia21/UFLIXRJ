from flask import Flask 
from app.extensions import db, migrate

from app.cadastro_alunos.routes import aluno_api
from app.cadastro_professores.routes import professor_api


def create_app():
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(professor_api)
    app.register_blueprint(aluno_api)


    return app