from app.cadastro_alunos.model import Aluno
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 
from flask import Blueprint
from flask import render_template, abort
from jinja2 import TemplateNotFound
from flask import redirect
from flask_jwt_extended import current_user

class AlunoCreate(MethodView): #/aluno

    def get(self):
        aluno = Aluno.query.all() #Accessing the data in database
        return render_template("CadastroAluno/cadastroAluno.html", logged_in_as=current_user)
        
    
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

        return redirect ('/login', logged_in_as=current_user)

class AlunoDetails(MethodView): #/aluno/<int:id>
    def get(self,id):
        aluno = Aluno.get_or_404(id)
        return aluno.json(),200

    def put(self,id):
        aluno = Aluno.get_or_404(id)
        data = request.json      
        nome = data['nome']
        email = data['email']
        cpf = data['cpf']
        dre = data['dre']
        curso = data['curso']
        senha = str(data['senha'])

        
        aluno.nome = nome
        aluno.email = email
        aluno.cpf = cpf
        aluno.dre = dre
        aluno.curso= curso
        aluno.senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
  
        db.session.commit()
        return aluno.json() , 200

    def patch(self,id):
        aluno = Aluno.query.get_or_404(id)
        dados = request.json 

        data = request.json    

        nome = data['nome', aluno.nome]
        email = data['email', aluno.email]
        cpf = data['cpf', aluno.cpf]
        dre = data['dre', aluno.dre]
        curso = data['curso', aluno.curso] 
        senha = str(data['senha'])      

        aluno.nome = nome
        aluno.email = email
        aluno.cpf = cpf
        aluno.dre = dre
        aluno.curso = curso
        aluno.senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())


        db.session.commit()
        return aluno.json() , 200

    def delete(self,id):
        aluno = Aluno.query.get_or_404(id)
        db.session.delete(aluno)
        db.session.commit()
        return aluno.json(), 200