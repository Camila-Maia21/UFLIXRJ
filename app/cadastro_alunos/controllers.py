from app.cadastro_alunos.model import Aluno
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 
from flask import Blueprint
from flask import render_template, abort
from jinja2 import TemplateNotFound
from flask import redirect

class AlunoCreate(MethodView): #/aluno

    def get(self):
        aluno = Aluno.query.all() #Accessing the data in database
        return render_template("CadastroAluno/cadastroAluno.html")
        
    
    def post(self): 
        data = request.form

        nome = data['nome']
        email = data['email']
        cpf = data['cpf']
        dre = data['dre']
        curso = data['curso']
        senha = str(data['senha'])

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(dre, str) or not isinstance(curso, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) #criptografa senha e adiciona um "sal"

        aluno = Aluno(nome=nome, email=email , cpf=cpf, dre=dre, curso=curso, senha_hash=senha_hash)

        db.session.add(aluno)
        db.session.commit()

        return redirect ('/login')

class AlunoDetails(MethodView): #/aluno/<int:id>
    
    def get(self, id):
        aluno = Aluno.query.all()
        return jsonify(aluno.json() for aluno in aluno), 200

    def patch(self, id):
        aluno = Aluno.query.all()
        data = request.json

        nome = data.get('nome', aluno.nome)
        email = data.get('email', aluno.email)
        cpf = data.get('cpf', aluno.cpf)
        dre = data.get('dre', aluno.dre)
        curso = data.get('curso', aluno.curso)
        senha = data.get('senha', aluno.senha)


        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(dre, str) or not isinstance(curso, str) or not isinstance(senha, str):
            return {"error" : "Algum tipo invalido"}, 400


        aluno.nome = nome
        aluno.email = email
        aluno.cpf = cpf
        aluno.dre = dre
        aluno.curso = curso
        aluno.senha = senha

        db.session.commit()