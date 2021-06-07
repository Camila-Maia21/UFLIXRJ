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

    aluno = Aluno.query.filter_by(cpf=cpf).first()
    professor = Professor.query.filter_by(cpf=cpf).first()
    if aluno and bcrypt.checkpw(senha.encode(), aluno.senha_hash):
        login_user(aluno)
    elif professor and bcrypt.checkpw(senha.encode(), professor.senha_hash):
        login_user(professor)
    else:
            flash('Please check your login details and try again.')
            return redirect('/login')

    return redirect ('/materia')

@login_api.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect ('/login')
'''
{{ current_user.nome }}
{{ current_user.nome }}
{{ if current_user==Usuario }}
<a> botao 1</a>
{{ elif current_user==Professor}}
<a> botao2 </a>
'''