from app.cadastro_alunos.model import Aluno
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 
from flask import Blueprint
from flask import render_template, abort
from jinja2 import TemplateNotFound
from flask import redirect
'''
app_aluno = Blueprint('simple_page', __name__, template_folder='templates')

@app_aluno.route('/aluno', defaults={'cadastroAluno': 'index'})
def criar_aluno():
    if request.method == 'POST':

        dados = request.json
        nome = dados.get('nome')
        email = dados.get('email')
        cpf = dados.get('cpf')
        dre = dados.get('dre')
        curso = dados.get('curso')
        senha = str(dados.get('senha'))

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(dre, str) or not isinstance(curso, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) #criptografa senha e adiciona um "sal"

        aluno = Aluno(nome=nome, email=email , cpf=cpf, dre=dre, curso=curso, senha_hash=senha_hash)

        db.session.add(aluno)
        db.session.commit()

    return aluno.json(), 200

@app_aluno.route('/aluno')
def rota_aluno(cadastroAluno):
    try:
        return render_template(f'template/cadastroAluno.html')
    except TemplateNotFound:
        abort(404)

    
'''
class AlunoDetails(MethodView): #/aluno

    def get(self):
        aluno = Aluno.query.all() #Accessing the data in database
        return render_template("CadastroAluno/cadastroAluno.html") #Transforma o objeto em json 
        
    
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

        return redirect('/login')