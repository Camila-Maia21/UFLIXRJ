from flask import Blueprint
from flask_login.utils import login_required
from app.minhas_disciplinas.controllers import (MinhasDisciplinas)

minhas_disciplinas_api = Blueprint('minhas_disciplinas_api', __name__)

minhas_disciplinas_api.add_url_rule(
    '/materia', view_func = MinhasDisciplinas.as_view('materia'), methods = ['GET']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)