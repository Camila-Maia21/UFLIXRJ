from app.materia.model import Materia
from app.extensions import db
from flask import request, render_template, redirect
from flask.views import MethodView 

class MateriaDetails(MethodView): #materia
    def get(self):
        materia = Materia.query.all() #Accessing the data in database
        return render_template("Minhasdisciplinas/MinhasDisciplinas.html") #Transforma o objeto em json 
    
    def post(self): 
        data = request.json

        nome = data.get('nome')
        periodo = data.get('periodo')
        codigo_materia = data.get('codigo_materia')
        codigo_turma = data.get('codigo_turma')

        if not isinstance(nome, str) or not isinstance(periodo, str) or not isinstance(codigo_materia, str) or not isinstance(codigo_turma, str):
            return {"error" : "Algum tipo invalido"}, 400

        materia = Materia(nome=nome, periodo=periodo , codigo_materia=codigo_materia, codigo_turma=codigo_turma)

        db.session.add(materia)
        db.session.commit()

        return redirect('/login')
