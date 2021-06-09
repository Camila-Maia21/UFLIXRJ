from app.extensions import db
from app.model import BaseModel

class InscricaoMateria(BaseModel): 
    __tablename_ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    codigo_turma = db.Column(db.String(5), nullable=False, unique = True)


    def json(self): 
        return {
            "codigo_turma": self.codigo_turma
        }