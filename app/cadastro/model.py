from app.model import BaseModel
from app.extensions import db
from flask_login import UserMixin
from app.relacionamentos.model import association_user_rel

class User(UserMixin, BaseModel): 
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    cpf = db.Column(db.String(50), nullable=False, unique = True)
    dre = db.Column(db.String(50), unique = True)
    siape = db.Column(db.String(50), unique = True)
    curso = db.Column(db.String(50))
    senha_hash = db.Column(db.String(280), nullable=False)
    classe = db.Column(db.Boolean())  
    
    criardisciplina = db.relationship("CriarDisciplina")
    relacionamento = db.relationship("Relacionamento", secondary=association_user_rel, back_populates="user")
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
            "siape": self.siape, 
            "curso": self.curso
        }