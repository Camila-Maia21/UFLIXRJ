from app.cadastro_materia.model import Materia
from app.extensions import db
from flask import request 
from flask.views import MethodView
import bcrypt 
from flask import Blueprint
from flask import render_template
from jinja2 import TemplateNotFound
from flask import redirect

class MateriaCurrent(MethodView): #/materia/current

    def get(self):
        materia = Materia.query.all() #Accessing the data in database
        return render_template("Minhasdisciplinas/MinhasDisciplinas.html") #Transforma o objeto em json 
        
class MateriaDetails(MethodView):   #/materia/criar
    def post(self): 
        data = request.form

        professor = data['professor']
        nome = data['nome']
        periodo = data['periodo']
        codigo_materia = data['codigo_materia']
        codigo_turma = data['codigo_turma']

        if not isinstance(professor, str) or not isinstance(nome, str) or not isinstance(periodo, str) or not isinstance(codigo_materia, str) or not isinstance(codigo_turma, str):
            return {"error" : "Algum tipo invalido"}, 400

        materia = Materia(professor=professor, nome=nome, periodo=periodo, codigo_materia=codigo_materia, codigo_turma=codigo_turma)

        db.session.add(materia)
        db.session.commit()

        return render_template("Login/Login.html")