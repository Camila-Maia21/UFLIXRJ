from app.extensions import db

association_table = db.Table('association', db.Model.metadata,
                            db.Column('aluno', db.Integer, db.ForeignKey('aluno.id')), 
                            db.Column('materia', db.Integer, db.ForeignKey('materia.id')))


association_table2 = db.Table('association2', db.Model.metadata,
                            db.Column('aluno', db.Integer, db.ForeignKey('aluno.id')), 
                            db.Column('professor', db.Integer, db.ForeignKey('professor.id')))