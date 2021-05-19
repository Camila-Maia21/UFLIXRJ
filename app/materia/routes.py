from flask import Blueprint
from app.materia.controllers import (MateriaDetails, MateriaCurrent)

materia_api = Blueprint('materia_api', __name__)

materia_api.add_url_rule(
    '/materia', view_func = MateriaCurrent.as_view('materia'), methods = ['GET']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)
materia_api.add_url_rule(
    '/materia/details', view_func = MateriaDetails.as_view('materia_details'), methods = ['POST']
)