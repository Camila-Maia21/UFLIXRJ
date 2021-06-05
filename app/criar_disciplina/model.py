from app.extensions import db
from app.model import BaseModel

class CriarDisciplina(BaseModel): 
    __tablename_ = 'criardisciplina'
    id = db.Column(db.Integer, primary_key=True)
    materia = db.Column(db.String(50), nullable=False)
    professor = db.Column(db.String(50), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    codigo_materia = db.Column(db.String(5), nullable=False, unique = True)
    codigo_turma = db.Column(db.String(5), nullable=False, unique = True)

    def json(self): 
        return {
            "materia": self.materia,
            "professor": self.professor,
            "periodo": self.periodo,
            "codigo_materia": self.codigo_materia,
            "codigo_turma": self.codigo_turma
        }