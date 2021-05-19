from app.cadastro_professores.model import Professor
from app.extensions import db
from flask import  request, render_template, redirect
from flask.views import MethodView
import bcrypt 

class ProfessorDetails(MethodView): #/professor
    def get(self):
        professor = Professor.query.all() #Accessing the data in database
        return render_template("CadastroProfessor/cadastroProfessor.html") #Transforma o objeto em json 

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

        return render_template("Login/Login.html")

        #redirect('/login')

        
