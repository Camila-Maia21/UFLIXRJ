from app.cadastro_professores.model import Professor
from app.extensions import db
from flask import  request, render_template, redirect
from flask.views import MethodView
import bcrypt 
from flask_jwt_extended import current_user

class ProfessorDetails(MethodView): #/professor
    def get(self):
        professor = Professor.query.all() #Accessing the data in database
        return render_template("CadastroProfessor/cadastroProfessor.html", user=current_user) 

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
        #professor = User... 

        db.session.add(professor)
        db.session.commit()

        return redirect ('/login', user=current_user)

class ProfessorDetails(MethodView): #/professor/<int:id>
    def get(self,id):
        professor = Professor.get_or_404(id)
        return professor.json(),200

    def put(self,id):
        professor = Professor.get_or_404(id)
        data = request.json      
        nome = data['nome']
        email = data['email']
        cpf = data['cpf']
        siape = data['siape']
        senha = str(data['senha'])

        
        professor.nome = nome
        professor.email = email
        professor.cpf = cpf
        professor.siape = siape
        professor.senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
        
        db.session.commit()
        return professor.json() , 200

    def patch(self,id):
        professor = Professor.query.get_or_404(id)
        data = request.json 

        data = request.json    

        nome = data['nome', professor.nome]
        email = data['email', professor.email]
        cpf = data['cpf', professor.cpf]
        siape = data['siape', professor.siape]
        senha = str(data['senha'])       

        professor.nome = nome
        professor.email = email
        professor.cpf = cpf
        professor.siape = siape
        professor.senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())


        db.session.commit()
        return professor.json() , 200

    def delete(self,id):
        professor = Professor.query.get_or_404(id)
        db.session.delete(professor)
        db.session.commit()
        return professor.json(), 200


        
