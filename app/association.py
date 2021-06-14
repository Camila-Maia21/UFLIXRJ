from app.extensions import db

association_table = db.Table('association', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('criardisciplina_id', db.Integer, db.ForeignKey('criardisciplina.id'))
)
