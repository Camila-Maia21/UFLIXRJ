from app.cadastro.model import User
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 
from flask import Blueprint
from flask import render_template, abort
from jinja2 import TemplateNotFound
from flask import redirect

class AlunoCreate(MethodView): #/cadastroaluno

    def get(self):
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

        aluno = User(nome=nome, email=email , cpf=cpf, dre=dre, curso=curso, senha_hash=senha_hash, classe = 0)

        db.session.add(aluno)
        db.session.commit()

        return redirect ('/login')



class ProfessorCreate(MethodView): #/cadatroprofessor
    def get(self):
        return render_template("CadastroProfessor/cadastroProfessor.html") 

    def post(self): 
        data = request.form
        nome = data['nome']
        email = data['email']
        cpf = data['cpf']
        siape = data['siape']
        senha = str(data['senha'])
        

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(siape, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) #criptografa senha e adiciona um "sal"

        professor = User(nome=nome, email=email , cpf=cpf, siape=siape, senha_hash=senha_hash, classe = 1)

        db.session.add(professor)
        db.session.commit()

        return redirect ('/login')

class UserDetails(MethodView): #/user/<int:id>
    def get(self,id):
        user = User.get_or_404(id)
        return user.json(),200

    def put(self,id):
        user = User.get_or_404(id)
        data = request.json      
        nome = data['nome']
        email = data['email']
        cpf = data['cpf']
        siape = data['siape']
        dre = data['dre']
        curso = data['curso']
        senha = str(data['senha'])

        
        user.nome = nome
        user.email = email
        user.cpf = cpf
        user.siape = siape
        user.curso = curso
        user.dre = dre
        user.senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
        
        db.session.commit()
        return user.json() , 200

    def patch(self,id):
        user = User.query.get_or_404(id)
        data = request.json 

        data = request.json    

        nome = data['nome', user.nome]
        email = data['email', user.email]
        cpf = data['cpf', user.cpf]
        siape = data['siape', user.siape]
        senha = str(data['senha'])       

        user.nome = nome
        user.email = email
        user.cpf = cpf
        user.siape = siape
        user.senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())


        db.session.commit()
        return user.json() , 200

    def delete(self,id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return user.json(), 200
