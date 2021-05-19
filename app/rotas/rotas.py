from app.cadastro_alunos.model import Aluno
from flask import Blueprint

aluno_api = Blueprint('alunos_api', __name__)

@aluno_api.route('/aluno', method=['POST'])
def criar_aluno():
    if request.method == 'POST':
        dados = request.json

        nome = dados.get('nome')

        aluno = Aluno(nome,)

        db.session.add(aluno)
        db.session.commit()

        return aluno.json(), 200    