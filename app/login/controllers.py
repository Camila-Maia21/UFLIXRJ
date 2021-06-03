from app.login.model import Login
from app.cadastro_professores.model import Professor
from app.cadastro_alunos.model import Aluno
from flask import request, render_template, redirect
from flask.views import MethodView
import bcrypt 
from flask_jwt_extended import current_user
from app.extensions import db, jwt

class UserLogin(MethodView):  #/login
    def get(self):
        return render_template("Login/Login.html")

    def post(self):
       
        dados = request.form

        cpf = dados.get('cpf')
        senha = str(dados.get('senha'))

        user = Aluno.query.filter_by(cpf=cpf).first() #acessa o banco de dados e filtra o que você quer da classe
        if user is None or not bcrypt.checkpw(senha.encode(), user.senha_hash):
            user = Professor.query.filter_by(cpf=cpf).first()
            if user is None or not bcrypt.checkpw(senha.encode(), user.senha_hash):
                return {'error': 'usuario nao existente'}

        return redirect ('/materia', user=current_user) 

        #Login User -> cria uma seção (carregar informações do usuário)
        #logout User -> encerra a seção
        #current_user.id
