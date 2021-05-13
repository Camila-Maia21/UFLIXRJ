from flask import Blueprint
from app.cadastro_professores.controllers import (ProfessorDetails)

professor_api = Blueprint('professor_api', __name__)

professor_api.add_url_rule(
    '/professor', view_func = ProfessorDetails.as_view('professor_details'), methods = ['GET', 'POST']
)
