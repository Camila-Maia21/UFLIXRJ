from app.cadastro_professores.model import Professor
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView

class ProfessorDetails(MethodView): #professor
    def get(self):
        professor = Professor.query.all()
        return jsonify(professor.json() for professor in professor), 200
    
    def post(self): 
        data = request.json

        nome = data.get('nome')
        email = data.get('email')
        cpf = data.get('cpf')
        siape = data.get('cpf')
        senha = data.get('senha')

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(siape, str):
            return {"error" : "Algum tipo invalido"}, 400

        professor = Professor(nome=nome, email=email , cpf=cpf, siape=siape)

        db.session.add(professor)
        db.session.commit()

        return professor.json(), 200
