from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from . import db
from app.cadastro_professores.model import Professor
from app.cadastro_alunos.model import Aluno
import bcrypt 
from flask_jwt_extended import create_access_token, current_user, jwt_required, get_jwt_identity
from app.cadastro_alunos.controllers import Aluno
from app.cadastro_professores.controllers import Professor

login_api = Blueprint('login_api', __name__)
main_api = Blueprint('main', __name__)
'''
@main_api.route('/profile')
@login_required
def profile():
    return render_template('profile.html', cpf=current_user.cpf)
'''
@login_api.route('/login')
def login():
    return render_template('login.html')

@login_api.route('/login', methods=['POST'])
def login_post():
    cpf = request.form.get('cpf')
    password = request.form.get('password')

    user = Professor.query.filter_by(cpf=cpf).first()
    if user is None or not user.check_password(user.password, password):
        user = Aluno.query.filter_by(cpf=cpf).first()
        if user is None or not user.check_password(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))

    login_user(user)
    return redirect ('/materia')

@login_api.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

'''
class UserLogin(MethodView):  #/login
    def get(self):
        return render_template("Login/Login.html")

    @jwt_required()
    def post(self):
       
        dados = request.form

        cpf = dados.get('cpf')
        senha = str(dados.get('senha'))

        user = Aluno.query.filter_by(cpf=cpf).first() #acessa o banco de dados e filtra o que você quer da classe
        token = create_access_token(identity=user.id)
        if user is None or not bcrypt.checkpw(senha.encode(), user.senha_hash):
            user = Professor.query.filter_by(cpf=cpf).first()
            token = create_access_token(identity=user.id)
            if user is None or not bcrypt.checkpw(senha.encode(), user.senha_hash):
                return {'error': 'usuario nao existente'} 
        
        current_user = get_jwt_identity()

        return redirect ('/materia', user=current_user)

        #Login User -> cria uma seção (carregar informações do usuário)
        #logout User -> encerra a seção
        #current_user
'''
