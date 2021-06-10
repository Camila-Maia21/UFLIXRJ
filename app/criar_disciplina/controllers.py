from app.criar_disciplina.model import CriarDisciplina
from app.extensions import db
from flask import request, render_template, redirect
from flask.views import MethodView
from flask_login import current_user, login_required

class CriarDisciplinaDetails(MethodView): #/criardisciplina
    def get(self):
            return render_template("CriarDisciplina/CriarDisciplina.html")

    def post(self): 
        data = request.form

        materia = data['materia']
        periodo = data['periodo']
        codigo_materia = data['codigo_materia']
        codigo_turma = data['codigo_turma']

        if not isinstance(materia, str) or not isinstance(periodo, str) or not isinstance(codigo_materia, str) or not isinstance(codigo_turma, str):
            return {"error" : "Algum tipo invalido"}, 400

        #professor_id=current_user.id

        criardisciplina = CriarDisciplina(materia=materia, periodo=periodo , codigo_materia=codigo_materia, codigo_turma=codigo_turma, user_id = current_user.id)

        db.session.add(criardisciplina)
        db.session.commit()

        return redirect('/materia')
        
class CriarDisciplinaEdit(MethodView): #/criardisciplina/edit/<int:id>
    def get(self,id):
        criardisciplina = CriarDisciplina.get_or_404(id)
        return criardisciplina.json(),200

    def put(self,id):
        criardisciplina = CriarDisciplina.get_or_404(id)
        data = request.json      
        materia = data['materia']
        professor = data['professor']
        periodo = data['periodo']
        codigo_materia = data['codigo_materia']
        codigo_turma = data['codigo_turma']

        
        criardisciplina.materia = materia
        criardisciplina.professor = professor
        criardisciplina.periodo = periodo
        criardisciplina.codigo_materia = codigo_materia
        criardisciplina.codigo_turma = codigo_turma
        
        db.session.commit()
        return criardisciplina.json() , 200

    def patch(self,id):
        criardisciplina = CriarDisciplina.query.get_or_404(id) 

        data = request.json    

        materia = data['materia', criardisciplina.materia]
        professor = data['professor', criardisciplina.professor]
        periodo = data['periodo', criardisciplina.periodo]
        codigo_materia = data['codigo_materia', criardisciplina.codigo_materia]
        codigo_turma = data['codigo_turma', criardisciplina.codigo_turma]       

        criardisciplina.materia = materia
        criardisciplina.professor = professor
        criardisciplina.periodo = periodo
        criardisciplina.codigo_materia = codigo_materia
        criardisciplina.codigo_turma = codigo_turma


        db.session.commit()
        return criardisciplina.json() , 200

    def delete(self,id):
        criardisciplina = CriarDisciplina.query.get_or_404(id)
        db.session.delete(criardisciplina)
        db.session.commit()
        return criardisciplina.json(), 200



    
