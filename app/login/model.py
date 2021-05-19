from app.model import BaseModel
from app.extensions import db 

class Login(BaseModel):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key = True)
    cpf = db.Column(db.String(50), nullable = False)
    senha_hash = db.Column(db.String(20), nullable = False) 