from app.model import BaseModel
from app.extensions import db
from app.association import association_table

class Materia(BaseModel): 
    __tablename_ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    codigo_materia = db.Column(db.String(5), nullable=False, unique = True)
    codigo_turma = db.Column(db.String(5), nullable=False, unique = True)

    professor_id = db.Column(db.Integer, db.ForeignKey('materia.id')) 
    aluno = db.relationship('Aluno', secondary=association_table, backref='materia')

    def json(self): 
        return {
            "nome": self.nome,
            "periodo": self.periodo,
            "codigo_materia": self.codigo_materia,
            "codigo_turma": self.codigo_turma
        }