from flask import Blueprint
from app.materia.controllers import (MateriaCurrent, MateriaDetails)

materia_api = Blueprint('materia_api', __name__)

materia_api.add_url_rule(
    '/materia/current', view_func = MateriaCurrent.as_view('materia_current'), methods = ['GET']
)

materia_api.add_url_rule(
    '/materia', view_func = MateriaDetails.as_view('materia_details'), methods = ['POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)