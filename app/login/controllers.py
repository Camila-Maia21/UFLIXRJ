from app.login.model import Login
from app.cadastro_professores.model import Professor
from app.cadastro_alunos.model import Aluno
from flask import request, render_template, redirect
from flask.views import MethodView
import bcrypt 
from flask_jwt_extended import create_access_token
from app.extensions import db 

class UserLogin(MethodView):  #/login
    def get(self):
        return render_template("Login/Login.html") #Transforma o objeto em json 

    def post(self):

        dados = request.json

        cpf = dados.get('cpf')
        senha = str(dados.get('senha'))

        aluno = Aluno.query.filter_by(cpf=cpf).first() #acessa o banco de dados e filtra o que você quer da classe
        professor = Professor.query.filter_by(cpf=cpf).first()

        print(aluno.nome)
        print(professor.nome)

        token = create_access_token(identity=aluno.id)
        token = create_access_token(identity=professor.id)

        return request.json
        
        #redirect ('/materia/current')

'''
        if aluno.nome != 'Camila':
            return {'error': 'Usuário não encontrado'}, 400

        if not professor or not bcrypt.checkpw(senha.encode(), professor.senha_hash):
            return {'error': 'Usuário não encontrado'}, 400
'''

        