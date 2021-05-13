from flask import Blueprint
from .controllers import (LoginDetails)

login_api = Blueprint('login_api', __name__)

login_api.add_url_rule(
    '/login', view_func= LoginDetails.as_view('login_details'), methods = ['GET', 'POST']
)
