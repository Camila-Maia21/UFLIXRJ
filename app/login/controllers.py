from app.login.model import Login
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 

class LoginDetails(MethodView): #login
    def get(self):
        login = Login.query.all()
        return jsonify(login.json() for login in login), 200


    def post(self):
        data = request.json

        cpf = data.get('cpf')
        senha = str(data.get('senha'))


        if not isinstance(cpf, str) or not isinstance(senha, str):
            return {"error" : "Algum tipo invalido"}, 400

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

        login = Login(cpf = cpf, senha_hash = senha_hash)

        db.session.add(login)
        db.session.commit()

        return login.json(), 200