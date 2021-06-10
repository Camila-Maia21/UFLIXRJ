from app.extensions import db
from app.model import BaseModel
#from app.association import association_table

class CriarDisciplina(BaseModel): 
    __tablename__ = "criardisciplina"
    id = db.Column(db.Integer, primary_key=True)
    materia = db.Column(db.String(50), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    codigo_materia = db.Column(db.String(5), nullable=False)
    codigo_turma = db.Column(db.String(5), nullable=False, unique = True)

    video = db.relationship("Video") 
    #user = db.relationship("User", secondary=association_table, back_populates="criardisciplina") 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def json(self): 
        return {
            "materia": self.materia,
            "periodo": self.periodo,
            "codigo_materia": self.codigo_materia,
            "codigo_turma": self.codigo_turma
        }