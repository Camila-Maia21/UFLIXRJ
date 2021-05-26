from app.cadastro_professores.model import Professor
from app.extensions import db
from flask import  request, render_template, redirect
from flask.views import MethodView
import bcrypt 
from flask import jsonify

class ProfessorDetails(MethodView): #/professor
    def get(self):
        professor = Professor.query.all() #Accessing the data in database
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

        professor = Professor(nome=nome, email=email , cpf=cpf, siape=siape, senha_hash=senha_hash)

        db.session.add(professor)
        db.session.commit()

        return redirect ('/login')

class ProfessorDetails(MethodView): #/professor/<int:id>
    
    def get(self, id):
        professor = Professor.query.all()
        return jsonify(professor.json() for professor in professor), 200

    def patch(self, id):
        professor = Professor.query.all()
        data = request.json

        nome = data.get('nome', professor.nome)
        email = data.get('email', professor.email)
        cpf = data.get('cpf', professor.cpf)
        siape = data.get('siape', professor.siape)
        senha = data.get('senha', professor.senha)


        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(siape, str) or not isinstance(senha, str):
            return {"error" : "Algum tipo invalido"}, 400


        professor.nome = nome
        professor.email = email
        professor.cpf = cpf
        professor.siape = siape
        professor.senha = senha

        db.session.commit()


        
