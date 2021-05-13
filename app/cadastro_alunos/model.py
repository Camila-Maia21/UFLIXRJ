from app.model import BaseModel
from app.extensions import db

class Aluno(BaseModel): 
    __tablename_ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    cpf = db.Column(db.String(50), nullable=False, unique = True)
    dre = db.Column(db.String(50), nullable=False, unique = True)
    curso = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.LargeBinary(280), nullable=False)