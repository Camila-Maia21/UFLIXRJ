from app.cadastro_alunos.model import Aluno
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 

class AlunoDetails(MethodView): #aluno
    def get(self):
        aluno = Aluno.query.all()
        return jsonify(aluno.json() for aluno in aluno), 200
        
    
    def post(self): 
        data = request.json

        nome = data.get('nome')
        email = data.get('email')
        cpf = data.get('cpf')
        dre = data.get('dre')
        curso = data.get('curso')
        senha = data.get('curso')

        if not isinstance(nome, str) or not isinstance(email, str) or not isinstance(cpf, str) or not isinstance(dre, str) or not isinstance(curso, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

        aluno = Aluno(nome=nome, email=email , cpf=cpf, dre=dre, curso=curso, senha=senha)

        db.session.add(aluno)
        db.session.commit()

        return aluno.json(), 200
