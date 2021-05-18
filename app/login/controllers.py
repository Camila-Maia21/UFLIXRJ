from app.login.model import Login
from app.cadastro_professores.model import Professor
from app.cadastro_alunos.model import Aluno
from flask import request 
from flask.views import MethodView
import bcrypt 
from flask_jwt_extended import create_access_token

class UserLogin(MethodView):  #/login
    def post(self):

        dados = request.json

        cpf = dados.get('cpf')
        senha = str(dados.get('senha'))

        aluno = Aluno.query.filter_by(cpf=cpf).first()
        professor = Professor.query.filter_by(cpf=cpf).first()

        token = create_access_token(identity=aluno.id)
        token2 = create_access_token(identity=professor.id)

        return {'token':token}, 200
'''
        if not aluno or not bcrypt.checkpw(senha.encode(), aluno.senha_hash):
            return {'error': 'Usuário não encontrado'}, 400

        if not professor or not bcrypt.checkpw(senha.encode(), professor.senha_hash):
            return {'error': 'Usuário não encontrado'}, 400
'''