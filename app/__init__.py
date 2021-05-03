from flask import Flask 

from app.cadastro_alunos.model import Alunos
from app.cadastro_professores.model import Professores



def create_app():
    app = Flask(__name__)