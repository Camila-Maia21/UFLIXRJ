from app.model import BaseModel
from app.extensions import db
from app.association import association_table2

class Professor(BaseModel): 
    __tablename_ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    cpf = db.Column(db.String(50), nullable=False, unique = True)
    siape = db.Column(db.String(50), nullable=False, unique = True)
    senha_hash = db.Column(db.LargeBinary(280), nullable=False)

    materia = db.relationship('Materia', backref='professor') 
    aluno = db.relationship('Aluno', secondary=association_table2, backref='professor')

    def json(self): 
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "siape": self.siape
        }