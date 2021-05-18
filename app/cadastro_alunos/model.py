from app.model import BaseModel
from app.extensions import db
from app.association import association_table, association_table2

class Aluno(BaseModel): 
    __tablename_ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    cpf = db.Column(db.String(50), nullable=False, unique = True)
    dre = db.Column(db.String(50), nullable=False, unique = True)
    curso = db.Column(db.String(50), nullable=False)
    senha_hash = db.Column(db.String(280), nullable=False)

    materia = db.relationship('Materia', secondary=association_table, backref='aluno')
    professor = db.relationship('Professor', secondary=association_table2, backref='aluno2')

    def json(self): 
        return {
            "nome": self.nome,
            "email": self.email,
            "cpf": self.cpf,
            "dre": self.dre,
            "curso": self.curso
        }