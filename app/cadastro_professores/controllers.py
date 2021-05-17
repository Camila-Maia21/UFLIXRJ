from app.cadastro_professores.model import Professor
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 

class ProfessorDetails(MethodView): #professor
    def get(self):
        professor = Professor.query.all()
        return jsonify([professor.json() for professor in professor]), 200
    
    def post(self): 
        data = request.json

        nome = data.get('nome')
        email = data.get('email')
        cpf = data.get('cpf')
        siape = data.get('cpf')
        senha = str(data.get('senha'))

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(siape, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

        professor = Professor(nome=nome, email=email , cpf=cpf, siape=siape, senha_hash=senha_hash)

        db.session.add(professor)
        db.session.commit()

        return professor.json(), 200
