from flask import Blueprint
from app.materia.controllers import (MateriaDetails)

materia_api = Blueprint('materia_api', __name__)

materia_api.add_url_rule(
    '/criardisciplina', view_func = MateriaDetails.as_view('criar_disciplina'), methods = ['GET', 'POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)