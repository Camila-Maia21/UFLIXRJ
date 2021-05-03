from app.cadastro_alunos.model import Alunos

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastroaluno", methods = ["POST", "GET"])
def cadastro():
    user = ""
    senha = ""

    if request.method  == "POST":
        user = request.form["fname"]
        senha = request.form["lname"]

        if user == "" or senha == "":
            return "<h1>Por favor cadastre user e senha</h1>"
        else:
            pessoa = Aluno(user,senha)
            pessoa.salva()
            return "<h1>Registro salvo com sucesso</h1>"

app.run()