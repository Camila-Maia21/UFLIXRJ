from app.materia.model import Materia
from app.extensions import db
from flask import request, render_template, redirect
from flask.views import MethodView


class MateriaDetails(MethodView): #/criardisciplina
    def get(self):
        materia = Materia.query.all() #Accessing the data in database
        return render_template("CriarDisciplina/CriarDisciplina.html") #Transforma o objeto em json 

    def post(self): 
        data = request.form

        nome = data['nome']
        periodo = data['periodo']
        codigo_materia = data['codigo_materia']
        codigo_turma = data['codigo_turma']

        if not isinstance(nome, str) or not isinstance(periodo, str) or not isinstance(codigo_materia, str) or not isinstance(codigo_turma, str):
            return {"error" : "Algum tipo invalido"}, 400

        materia = Materia(nome=nome, periodo=periodo , codigo_materia=codigo_materia, codigo_turma=codigo_turma)

        db.session.add(materia)
        db.session.commit()

        return redirect('/materia')

        #return redirect('/login')


    
