from app.criar_disciplina.model import CriarDisciplina
from app.cadastro.model import User
from flask import request 
from flask.views import MethodView
from flask import render_template
from flask import redirect

class InscricaoDisciplina(MethodView): #/inscricaodisciplina/<int:materia_id>
    def get(self):
        return render_template("InscricaoDisciplina/inscricaodisciplina.html")

    def post(self, codigo_turma):
        codigo_turma_materia = codigo_turma
        materia = CriarDisciplina.query.filter_by(codigo_turma=codigo_turma)
        if materia == codigo_turma: 
            user = User.query.filter_by(criardisciplina_id = codigo_turma_materia)

        return redirect('/materia')

    #current_user.materias 
    #query.all(id) == current.user.id