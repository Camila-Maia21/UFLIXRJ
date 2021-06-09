from flask import Flask, redirect, render_template
from app.extensions import db, jwt, migrate, login_manager
from app.config import Config
from flask_login import login_required
from app.criar_disciplina.model import CriarDisciplina
from app.criar_video.model import Video

from app.cadastro_alunos.routes import aluno_api
from app.cadastro_professores.routes import professor_api
from app.criar_disciplina.routes import criar_disciplina_api
from app.login.controllers import login_api, main_api
from app.minhas_disciplinas.routes import minhas_disciplinas_api
from app.criar_video.routes import video_api

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
    app.config.from_object(Config)
    login_manager.login_view = 'login.controllers.login'
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    login_manager.init_app(app)
    
    app.register_blueprint(professor_api)
    app.register_blueprint(aluno_api)
    app.register_blueprint(criar_disciplina_api)
    app.register_blueprint(login_api)
    app.register_blueprint(minhas_disciplinas_api)
    app.register_blueprint(main_api)
    app.register_blueprint(video_api)

    from app.cadastro_professores.model import Professor
    from app.cadastro_alunos.model import Aluno

    @login_manager.user_loader
    def load_user(cpf):
        if Aluno.query.get(cpf):
            access  = Aluno.query.get(cpf)
        else:
            access = Professor.query.get(cpf)
        return access

    @app.route('/')
    def pagina_inicial():
        return redirect ("/login")

    @app.route('/materia/<id>')
    @login_required
    def materia_especifica(id):
        id_materia = id
        materia = CriarDisciplina.query.filter_by(id = id_materia).first()
        videos = Video.query.filter_by(criardisciplina_id = id_materia).first()
        return render_template ("Disciplina/Disciplina.html", materia= materia, videos = videos)

    @app.route('/materia/video')
    @login_required
    def video_materia():
        return render_template ("Video/video.html")

    return app

''' 
    @app.route('/materia/<materia>')
    @login_required
    def materia_especifica(materia):
        return render_template ("Disciplina/Disciplina.html", materia)
'''