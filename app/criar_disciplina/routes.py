from flask import Blueprint
from app.criar_disciplina.controllers import (CriarDisciplinaDetails)

criar_disciplina_api = Blueprint('criar_disciplina_api', __name__)

criar_disciplina_api.add_url_rule(
    '/criardisciplina', view_func = CriarDisciplinaDetails.as_view('criardisciplina_details'), methods = ['GET', 'POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)