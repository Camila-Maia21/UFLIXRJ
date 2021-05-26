from flask import Blueprint
from app.criar_disciplina.controllers import (CriarDisciplinaDetails)

criar_disciplina = Blueprint('criar_disciplina', __name__)

criar_disciplina.add_url_rule(
    '/criardisciplina', view_func = CriarDisciplinaDetails.as_view('criar_disciplina'), methods = ['GET', 'POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)