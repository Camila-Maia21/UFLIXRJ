from app.criar_disciplina.model import CriarDisciplina
from app.extensions import db
from flask import request, render_template, redirect
from flask.views import MethodView


class MinhasDisciplinas(MethodView): #/materia

    def get(self):
        materia = CriarDisciplina.query.all() #Accessing the data in database
        return render_template("Minhasdisciplinas/MinhasDisciplinas.html", materias=materia)