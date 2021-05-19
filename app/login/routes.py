from flask import Blueprint
from .controllers import (UserLogin)

login_api = Blueprint('login_api', __name__)

login_api.add_url_rule(
    '/login', view_func= UserLogin.as_view('login_details'), methods = ['GET','POST']
)
#view_func -> responde as solicitações de seu aplicativo (requisições)
