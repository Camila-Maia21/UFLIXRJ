from flask import Blueprint
from app.cadastro_professores.controllers import (ProfessorCurrent, ProfessorDetails)

professor_api = Blueprint('professor_api', __name__)

professor_api.add_url_rule(
    '/professor', view_func = ProfessorCurrent.as_view('professor_current'), methods = ['GET', 'POST']
)
professor_api.add_url_rule(
    '/professor/<int:id>', view_func = ProfessorDetails.as_view('professor_details'), methods = ['GET', 'PUT', 'PATCH', 'DELETE']
)
