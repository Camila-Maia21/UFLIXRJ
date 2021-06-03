from app.cadastro_materia.model import Materia
from app.extensions import db
from flask import request 
from flask.views import MethodView
from flask import render_template
from jinja2 import TemplateNotFound
from flask import redirect
from flask_jwt_extended import current_user

class MateriaCurrent(MethodView): #/materia/current

    def get(self):
        materia = Materia.query.all() #Accessing the data in database
        return render_template("Minhasdisciplinas/MinhasDisciplinas.html", user=current_user) 
        
class MateriaDetails(MethodView):   #/materia/criar
    def post(self): 
        data = request.form

        professor = data['professor']
        nome = data['nome']
        periodo = data['periodo']
        codigo_materia = data['codigo_materia']
        codigo_turma = data['codigo_turma']

        if not isinstance(professor, str) or not isinstance(nome, str) or not isinstance(periodo, str) or not isinstance(codigo_materia, str) or not isinstance(codigo_turma, str):
            return {"error" : "Algum tipo invalido"}, 400

        materia = Materia(professor=professor, nome=nome, periodo=periodo, codigo_materia=codigo_materia, codigo_turma=codigo_turma)

        db.session.add(materia)
        db.session.commit()

        return redirect('/login', user=current_user)

class MateriaEdit(MethodView): #/materia/edit/<int:id>
    def get(self,id):
        materia = Materia.get_or_404(id)
        return materia.json(),200

    def put(self,id):
        materia = Materia.get_or_404(id)
        data = request.json      
        professor = data['professor']
        nome = data['nome']
        periodo = data['periodo']
        codigo_materia = data['codigo_materia']
        codigo_turma = data['codigo_turma']

        materia.professor = professor
        materia.nome = nome
        materia.periodo = periodo
        materia.codigo_materia = codigo_materia
        materia.codigo_turma = codigo_turma
        
        db.session.commit()
        return materia.json() , 200

    def patch(self,id):
        materia = Materia.query.get_or_404(id)
        dados = request.json 

        data = request.json    
        professor = data['professor', materia.professor]
        nome = data['nome', materia.nome]
        periodo = data['periodo', materia.periodo]
        codigo_materia = data['codigo_materia', materia.codigo_materia]
        codigo_turma = data['codigo_turma', materia.codigo_turma]       

        materia.professor = professor
        materia.nome = nome
        materia.periodo = periodo
        materia.codigo_materia = codigo_materia
        materia.codigo_turma = codigo_turma


        db.session.commit()
        return materia.json() , 200

    def delete(self,id):
        materia = Materia.query.get_or_404(id)
        db.session.delete(materia)
        db.session.commit()
        return materia.json(), 200

    #current_user.materias 
    #query.all(id) == current.user.id
    #many to many -> aluno para materias
    #one to many -> professor para materias