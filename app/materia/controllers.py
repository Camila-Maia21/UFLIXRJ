from app.materia.model import Materia
from app.extensions import db
from flask import jsonify, request 
from flask.views import MethodView
import bcrypt 
from app.permissions import professor_jwt_required

class MateriaCurrent(MethodView): #materia/current
    def get(self):
        materia = Materia.query.all()
        return jsonify(materia.json() for materia in materia), 200

class MateriaDetails(MethodView): #materia

    decorators = [professor_jwt_required]
    
    def post(self): 
        data = request.json

        nome = data.get('nome')
        periodo = data.get('periodo')
        codigo_materia = data.get('codigo_materia')
        codigo_turma = data.get('codigo_turma')

        if not isinstance(nome, str) or not isinstance(periodo, str) or not isinstance(codigo_materia, str) or not isinstance(codigo_turma, str):
            return {"error" : "Algum tipo invalido"}, 400

        materia = Materia(nome=nome, periodo=periodo , codigo_materia=codigo_materia, codigo_turma=codigo_turma)

        db.session.add(materia)
        db.session.commit()

        return materia.json(), 200