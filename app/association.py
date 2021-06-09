from app.extensions import db

association_table = db.Table('association', db.Model.metadata,
    db.Column('aluno_id', db.Integer, db.ForeignKey('aluno.id')),
    db.Column('criardisciplina_id', db.Integer, db.ForeignKey('criardisciplina.id'))
)