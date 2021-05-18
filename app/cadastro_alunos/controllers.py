from app.cadastro_alunos.model import Aluno
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 
from flask import Blueprint
from flask import render_template, abort
from jinja2 import TemplateNotFound

class AlunoDetails(MethodView): #/aluno
    def get(self):
        aluno = Aluno.query.all() #Accessing the data in database
        return jsonify([aluno.json() for aluno in aluno]), 200 #Transforma o objeto em json 
        
    
    def post(self): 
        data = request.json 

        nome = data.get('nome')
        email = data.get('email')
        cpf = data.get('cpf')
        dre = data.get('dre')
        curso = data.get('curso')
        senha = str(data.get('senha'))

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(dre, str) or not isinstance(curso, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) #criptografa senha e adiciona um "sal"

        aluno = Aluno(nome=nome, email=email , cpf=cpf, dre=dre, curso=curso, senha_hash=senha_hash)

        db.session.add(aluno)
        db.session.commit()

        return aluno.json(), 200


aluno_api = Blueprint('aluno_api', __name__,template_folder='template')

@aluno_api.route('/aluno', defaults={'page': 'cadastroAluno'})
@aluno_api.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/cadastroAluno.html')
    except TemplateNotFound:
        abort(404)