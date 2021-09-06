from datetime import datetime

from db import db


class Alert(db.Model):
    __tablename__ = 'alert'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float(precision=2))
    field = db.Column(db.String(80))
    entity = db.Column(db.String(80))
    condition = db.Column(db.String(80))

    sended = db.Column(db.Boolean, default=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, value,field,entity,condition):
        self.entity = entity
        self.value = value
        self.field = field
        self.condition = condition

    def json(self):
        return {
            'id': self.id,
            'entity': self.entity,
            'sended': self.sended,
            'time_date': self.time_stamp
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_pending(cls):
        return cls.query.filter_by(sended=False).firts()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
