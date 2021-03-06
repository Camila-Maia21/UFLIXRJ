from app.cadastro_professores.model import Professores
from flask import render_template, request  
from flask import Blueprint 

professores_api = Blueprint('professores_api', __name__)
@app.route("/professores")
def cadastroP():
    return render_template("cadastro_professores.html")

@app.route("/cadastroprofessores", methods = ["POST", "GET"])
def cadastroprofessores():
    nome = ""
    cpf = "" 
    email = ""
    senha = ""
    siape = ""

    if request.method  == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        cpf = request.form["cpf"]
        senha = request.form["senha"]
        siape = request.form["siape"]

        if nome == "" or senha == "" or cpf == "":
            return "<h1>Todos os campos são obrigatórios</h1>"
        else:
            pessoa = Professores(nome,email,cpf,senha,siape)
            pessoa.salva()
            return "<h1>Registro salvo com sucesso</h1>"

app.run()
