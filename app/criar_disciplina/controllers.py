from app.criar_disciplina.model import Materia
from app.extensions import db
from flask import request, render_template, redirect
from flask.views import MethodView
from app.cadastro_alunos.model import Aluno
from app.cadastro_professores.model import Professor

class CriarDisciplinaDetails(MethodView): #/criardisciplina
    def get(self):
        #materia = Materia.query.all() #Accessing the data in database
        if Aluno:
            return render_template("AdicionarDisciplina/AdiconarDisciplina.html")
        elif Professor:
            return render_template("CriarDisciplina/CriarDisciplina.html")

    def post(self): 
        data = request.form

        materia = data['materia']
        professor = data['professor']
        periodo = data['periodo']
        codigo_materia = data['codigo_materia']
        codigo_turma = data['codigo_turma']

        if not isinstance(materia, str) or not isinstance(periodo, str) or not isinstance(codigo_materia, str) or not isinstance(codigo_turma, str):
            return {"error" : "Algum tipo invalido"}, 400

        materia = Materia(materia=materia, professor=professor, periodo=periodo , codigo_materia=codigo_materia, codigo_turma=codigo_turma)

        db.session.add(materia)
        db.session.commit()

        return redirect('/materia')


    
