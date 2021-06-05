from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
import bcrypt 
from werkzeug.security import generate_password_hash, check_password_hash
from app.cadastro_professores.model import Professor
from app.cadastro_alunos.model import Aluno
from app.extensions import db

login_api = Blueprint('login_api', __name__)
main_api = Blueprint('main', __name__)
cadastro_api = Blueprint('cadastro', __name__)
'''
@main_api.route('/profile')
@login_required
def profile():
    return render_template('profile.html', cpf=current_user.cpf)
'''
@login_api.route('/login')
def login():
    return render_template("Login/Login.html")

@login_api.route('/login', methods=['POST'])
def login_post():
    cpf = request.form.get('cpf')
    senha = request.form.get('senha')

    user = Professor.query.filter_by(cpf=cpf).first()
    if not user and not bcrypt.checkpw(senha.encode(), user.senha_hash):
        user = Aluno.query.filter_by(cpf=cpf).first()
        if not user and not bcrypt.checkpw(senha.encode(), user.senha_hash):
            flash('Please check your login details and try again.')
            return redirect('/login')

    login_user(user)
    return redirect ('/materia')

@login_api.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
#if user is None or not bcrypt.checkpw(senha.encode(), login.senha_hash):
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
