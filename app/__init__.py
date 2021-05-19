from flask import Flask, redirect, render_template
from app.extensions import db, migrate, jwt
from app.config import Config

from app.cadastro_alunos.routes import aluno_api
from app.cadastro_professores.routes import professor_api
from app.materia.routes import materia_api
from app.login.routes import login_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    app.register_blueprint(professor_api)
    app.register_blueprint(aluno_api)
    app.register_blueprint(materia_api)
    app.register_blueprint(login_api)

    @app.route('/')
    def pagina_inicial():
        return redirect ("/login")
    
    @app.route('/materia/<nome>')
    def materia_especifica(nome):
        return render_template ("Disciplinas/Disciplinas.html")

    return app