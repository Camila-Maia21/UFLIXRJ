from app.login.model import Login
from app.cadastro_professores.model import Professor
from app.cadastro_alunos.model import Aluno
from flask import request, render_template, redirect
from flask.views import MethodView
import bcrypt 
from flask_jwt_extended import create_access_token, current_user
from app.extensions import db, jwt

class UserLogin(MethodView):  #/login
    def get(self):
        return render_template("Login/Login.html")

    def post(self):
       
        dados = request.form

        cpf = dados.get('cpf')
        senha = str(dados.get('senha'))

        aluno = Aluno.query.filter_by(cpf=cpf).first() #acessa o banco de dados e filtra o que você quer da classe
        professor = Professor.query.filter_by(cpf=cpf).first()

        if aluno and bcrypt.checkpw(senha.encode(), aluno.senha_hash):
            token = create_access_token(identity=aluno.id)
        elif professor and bcrypt.checkpw(senha.encode(), professor.senha_hash):
            token = create_access_token(identity=professor.id)
        else:
            return {'error': 'usuario nao existente'}

        return redirect ('/materia')


