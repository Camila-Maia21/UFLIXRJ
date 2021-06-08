from app.extensions import db
from app.model import BaseModel

class CriarDisciplina(BaseModel): 
    __tablename_ = 'criardisciplina'
    id = db.Column(db.Integer, primary_key=True)
    materia = db.Column(db.String(50), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    codigo_materia = db.Column(db.String(5), nullable=False, unique = True)
    codigo_turma = db.Column(db.String(5), nullable=False, unique = True)

    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'))

    def json(self): 
        return {
            "materia": self.materia,
            "periodo": self.periodo,
            "codigo_materia": self.codigo_materia,
            "codigo_turma": self.codigo_turma
        }