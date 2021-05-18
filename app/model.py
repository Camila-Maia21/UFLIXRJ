from app.extensions import db 
from flask import jsonify, make_response, abort 
from sqlalchemy.exc import IntegrityError

class BaseModel(db.Model):

    __abstract__ = True

    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.add(self)
        
        try:
            db.session.commit()

        except IntegrityError as err:
            db.session.rollback()  #reverter o que foi feito (não salva)
            abort(make_response(jsonify({'errors': str(err.orig)}), 400))  