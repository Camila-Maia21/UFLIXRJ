from app.model import BaseModel
from app.extensions import db
from flask_login import UserMixin

class Professor(UserMixin, BaseModel): 
    __tablename_ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    cpf = db.Column(db.String(50), nullable=False, unique = True)
    siape = db.Column(db.String(50), nullable=False, unique = True)
    senha_hash = db.Column(db.LargeBinary(280), nullable=False)

    criardisciplina = db.relationship('CriarDisciplina', backref='professor')

    def json(self): 
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "siape": self.siape
        }