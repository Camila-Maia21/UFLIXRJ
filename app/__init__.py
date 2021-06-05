from flask import Flask, redirect, render_template
from app.extensions import db, migrate, jwt
from app.config import Config
from flask_jwt_extended import current_user
from flask_jwt_extended import JWTManager

from app.cadastro_alunos.routes import aluno_api
from app.cadastro_professores.routes import professor_api
from app.criar_disciplina.routes import criar_disciplina
from app.login.controllers import login_api
from app.minhas_disciplinas.routes import minhas_disciplinas_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    jwt = JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    
    app.register_blueprint(professor_api)
    app.register_blueprint(aluno_api)
    app.register_blueprint(criar_disciplina)
    app.register_blueprint(login_api)
    app.register_blueprint(minhas_disciplinas_api)

    @app.route('/')
    def pagina_inicial():
        return redirect ("/login")
    
    @app.route('/materia/<nome>')
    def materia_especifica(nome):
        return render_template ("Disciplina/Disciplina.html")

    @app.route('/materia/video')
    def video_materia():
        return render_template ("Video/video.html")

    return app