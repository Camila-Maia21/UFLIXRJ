from app.criar_disciplina.model import CriarDisciplina
from app.extensions import db
from flask import request, render_template, redirect
from flask.views import MethodView
from flask_login import current_user


class MinhasDisciplinas(MethodView): #/materia

    def get(self):
        materia = CriarDisciplina.query.filter_by(professor_id = current_user.id) #Accessing the data in database
        return render_template("Minhasdisciplinas/MinhasDisciplinas.html", materias=materia)