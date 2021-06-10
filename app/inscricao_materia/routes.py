from flask import Blueprint
from app.inscricao_materia.controllers import (InscricaoDisciplina)

inscricao_materia_api = Blueprint('inscricao_materia_api', __name__)

inscricao_materia_api.add_url_rule(
    '/inscricaodisciplina', view_func = InscricaoDisciplina.as_view('inscricaodisciplina_details'), methods = ['GET', 'POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)