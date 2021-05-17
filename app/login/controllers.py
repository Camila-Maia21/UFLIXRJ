from app.login.model import Login
from app.cadastro_professores.model import Professor
from app.cadastro_alunos.model import Aluno
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

class UserLogin(MethodView):  #/login
    def post(self):
        dados = request.json

        email = dados.get('email')
        password = str(dados.get('password'))

        aluno = Aluno.query.filter_by(email=email).first()
        professor = Professor.query.filter_by(email=email).first()

        if not aluno or not bcrypt.checkpw(password.encode(), aluno.password_hash):
            return {'error': 'Usuário não encontrado'}, 400

        if not professor or not bcrypt.checkpw(password.encode(), professor.password_hash):
            return {'error': 'Usuário não encontrado'}, 400

        token = create_access_token(identity=aluno.id)
        token = create_access_token(identity=professor.id)

        return {'token':token}, 200

'''
class LoginDetails(MethodView): #login
    def get(self):
        login = Login.query.all()
        return jsonify(login.json() for login in login), 200


    def post(self):
        data = request.json

        cpf = data.get('cpf')
        senha = str(data.get('senha'))


        if not isinstance(cpf, str) or not isinstance(senha, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

        login = Login(cpf = cpf, senha_hash = senha_hash)

        db.session.add(login)
        db.session.commit()

        return login.json(), 200

class UsuarioLogin(MethodView): #usuariologin
    def post(self): 
        data = request.json

        email = data.get('email')
        senha = str(data.get('senha'))

        login = Login.query.filter_by(email= email).first()

        if not login or not bcrypt.checkpw(senha.encode(), login.senha_hash):
            return{"error": "Usuario não encontrado"}, 400


        token = create_access_token(identity=login.id)
        
        return {"token": token}, 200
'''