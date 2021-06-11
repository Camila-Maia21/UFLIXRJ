from app.model import BaseModel
from app.extensions import db
from flask_login import UserMixin

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
    relacionamento_id = db.Column(db.Integer, db.ForeignKey('relacionamento.id'))
    relacionamento = db.relationship("Relacionamento", back_populates="user")
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