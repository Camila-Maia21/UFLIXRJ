from app.login.model import Login
from app.cadastro_professores.model import Professor
from app.cadastro_alunos.model import Aluno
from app.extensions import db
from flask import request 
from flask.views import MethodView
import bcrypt 
from flask_jwt_extended import create_access_token

class UserLogin(MethodView):  #/login
    def post(self):
        dados = request.json

        cpf = dados.get('cpf')
        senha = str(dados.get('senha'))

        login = Login.query.filter_by(cpf= cpf).first()

        if not login or not bcrypt.checkpw(senha.encode(), login.senha_hash):
            return{"error": "Usuario não encontrado"}, 400

        token = create_access_token(identity=login.id)

        return {'token':token}, 200
'''
        aluno = Aluno.query.filter_by(cpf=cpf).first()
        professor = Professor.query.filter_by(cpf=cpf).first()

        if not aluno or not bcrypt.checkpw(senha.encode(), aluno.senha_hash):
            return {'error': 'Usuário não encontrado'}, 400

        if not professor or not bcrypt.checkpw(senha.encode(), professor.senha_hash):
            return {'error': 'Usuário não encontrado'}, 400
'''