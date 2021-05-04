from app.cadastro_alunos.model import Alunos
from flask import render_template, request
from flask import Blueprint

alunos_api = Blueprint('alunos_api', __name__)
@app.route("/alunos")
def cadastroA():
    return render_template("cadastro_alunos.html")

@app.route("/cadastroalunos", methods = ["POST", "GET"])
def cadastroalunos():
    nome = ""
    senha = ""

    if request.method  == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        cpf = request.form["cpf"]
        senha = request.form["senha"]
        dre = request.form["dre"]
        curso = request.form["curso"]

        if nome == "" or senha == "" or cpf == "":
            return "<h1>Todos os campos são obrigatórios</h1>"
        else:
            pessoa = Alunos(nome, email, cpf, senha, dre, curso)
            pessoa.salva()
            return "<h1>Registro salvo com sucesso</h1>"

app.run()