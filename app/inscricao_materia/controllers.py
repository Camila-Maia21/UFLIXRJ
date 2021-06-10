from app.criar_disciplina.model import CriarDisciplina
from app.cadastro.model import User
from app.extensions import db
from flask import request 
from flask.views import MethodView
from flask import render_template
from jinja2 import TemplateNotFound
from flask import redirect

class InscricaoDisciplina(MethodView): #/inscricaodisciplina 
    def get(self):
        return render_template("InscricaoDisciplina/inscricaodisciplina.html") 
    def post(self): 
        codigo_turma = request.form.get('codigo_turma')
        materia = CriarDisciplina.query.filter_by(codigo_turma=codigo_turma).first()
        if materia.codigo_turma == codigo_turma:
            User.criardisciplina.id = materia.id
        return redirect('/materia')

    #current_user.materias 
    #query.all(id) == current.user.id
    #many to many -> aluno para materias
    #one to many -> professor para materias

    