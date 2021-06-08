from app.extensions import db
from app.model import BaseModel

class Materia(BaseModel): 
    __tablename_ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    professor = db.Column(db.String(5), nullable=False, unique = True)
    nome = db.Column(db.String(50), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    codigo_materia = db.Column(db.String(5), nullable=False, unique = True)
    codigo_turma = db.Column(db.String(5), nullable=False, unique = True)


    def json(self): 
        return {
            "professor": self.professor,
            "nome": self.nome,
            "periodo": self.periodo,
            "codigo_materia": self.codigo_materia,
            "codigo_turma": self.codigo_turma
        }