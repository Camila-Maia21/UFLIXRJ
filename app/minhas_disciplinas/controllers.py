from app.inscricao_materia.model import Relacionamento
from app.criar_disciplina.model import CriarDisciplina
from app.cadastro.model import User
from app.extensions import db
from flask import request, render_template, redirect
from flask.views import MethodView
from flask_login import current_user


class MinhasDisciplinas(MethodView): #/materia

    def get(self):
        user_id = current_user.id
        materia = CriarDisciplina.query.filter_by(user_id = user_id) #Accessing the data in database
        inscricoes = Relacionamento.query.filter_by(user = current_user).first()
        return render_template("Minhasdisciplinas/MinhasDisciplinas.html", materias=materia, inscricoes=inscricoes) 