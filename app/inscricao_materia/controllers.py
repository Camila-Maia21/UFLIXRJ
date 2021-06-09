from app.criar_disciplina.model import CriarDisciplina
from app.cadastro_alunos.model import Aluno
from app.extensions import db
from flask import request 
from flask.views import MethodView
from flask import render_template
from jinja2 import TemplateNotFound
from flask import redirect

class InscricaoDisciplina(MethodView): #/inscricaodisciplina 
    def post(self): 
        codigo_turma = request.form.get('codigo_turma')
        materia = CriarDisciplina.query.filter_by(codigo_turma=codigo_turma).first()
        if materia:
            materia = Aluno.criardisciplina
        return redirect('/login')

    #current_user.materias 
    #query.all(id) == current.user.id
    #many to many -> aluno para materias
    #one to many -> professor para materias