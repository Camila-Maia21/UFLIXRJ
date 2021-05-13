from app.model import BaseModel
from app.extensions import db

class Professor(BaseModel): 
    __tablename_ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    cpf = db.Column(db.String(50), nullable=False, unique = True)
    siape = db.Column(db.String(50), nullable=False, unique = True)
    senha = db.Column(db.LargeBinary(280), nullable=False)