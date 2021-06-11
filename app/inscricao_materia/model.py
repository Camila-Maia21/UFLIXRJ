from app.extensions import db
from app.model import BaseModel

association_disc_rel = db.Table('association_disc_rel', db.Model.metadata,
    db.Column('criardisciplina_id', db.Integer, db.ForeignKey('criardisciplina.id')),
    db.Column('relacionamento_id', db.Integer, db.ForeignKey('relacionamento.id'))
)

class Relacionamento(BaseModel):
    __tablename__ = "relacionamento"
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship("User", uselist=False, back_populates="relacionamento")
    criardisciplina = db.relationship("CriarDisciplina", secondary=association_disc_rel, back_populates="relacionamento")

