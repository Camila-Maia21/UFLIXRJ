from app.model import BaseModel
from app.extensions import db
from flask_login import UserMixin
from app.association import association_table

class Aluno(UserMixin, BaseModel): 
    __tablename__ = "aluno"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    cpf = db.Column(db.String(50), nullable=False, unique = True)
    dre = db.Column(db.String(50), nullable=False, unique = True)
    curso = db.Column(db.String(50), nullable=False)
    senha_hash = db.Column(db.String(280), nullable=False)

    criardisciplina = db.relationship("CriarDisciplina", secondary=association_table, back_populates="aluno")

    #role 
    '''
    {% if current_user.role is_authenticated %}
     Hi {{ current_user.nome }}!
     {% endif %}
    '''

    def json(self): 
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "dre": self.dre, 
            "curso": self.curso
        }