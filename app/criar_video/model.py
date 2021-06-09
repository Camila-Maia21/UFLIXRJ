from app.extensions import db
from app.model import BaseModel

class Video(BaseModel): 
    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(5), nullable=False)

    criardisciplina_id = db.Column(db.Integer, db.ForeignKey('criardisciplina.id'))

    def json(self): 
        return {
            "nome": self.nome,
            "descricao": self.descricao,
            "link": self.link
        }