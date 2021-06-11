from app.criar_disciplina.model import CriarDisciplina
from app.inscricao_materia.model import Relacionamento
from app.cadastro.model import User
from flask import request
from flask.views import MethodView
from flask import render_template
from flask import redirect
from flask_login import current_user
from app.extensions import db 

class InscricaoDisciplina(MethodView): #/inscricaodisciplina/<codigo_turma>
    def get(self):
        return render_template("InscricaoDisciplina/inscricaodisciplina.html")

    def post(self):
        data = request.form
        codigo_turma_forms = data['codigo_turma']
        materia = CriarDisciplina.query.filter_by(codigo_turma=codigo_turma_forms).first()
        if materia:
            user = current_user
            relacionamento = Relacionamento.query.filter_by(user=user).first()
            if relacionamento:
                relacionamento.criardisciplina.extend([materia])
            else:
                relacionamento = Relacionamento(user=user, criardisciplina = [materia])

            db.session.add(relacionamento)
            db.session.commit()

            return redirect('/materia')

    #current_user.materias 
    #query.all(id) == current.user.id