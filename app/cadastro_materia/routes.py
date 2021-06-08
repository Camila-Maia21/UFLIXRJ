from flask import Blueprint
from app.cadastro_materia.controllers import (MateriaCurrent, MateriaDetails)

cadastro_materia_api = Blueprint('materia_api', __name__)

cadastro_materia_api.add_url_rule(
    '/materia/current', view_func = MateriaCurrent.as_view('materia_current'), methods = ['GET']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)
cadastro_materia_api.add_url_rule(
    '/materia/cadastro', view_func = MateriaDetails.as_view('materia_cadastro'), methods = ['POST']
)