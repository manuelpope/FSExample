from datetime import datetime

from Factory import db


class AlertModel(db.Model):
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float(precision=2))
    field = db.Column(db.String(80))
    entity = db.Column(db.String(80))
    condition = db.Column(db.String(80))
    sended = db.Column(db.Boolean, default=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, value, field, entity, condition):
        self.entity = entity
        self.value = value
        self.field = field
        self.condition = condition

    def json(self):
        return {
            'id': self.id,
            'entity': self.entity,
            'sended': self.sended,
            'time_date': str(self.time_stamp.strftime("%m/%d/%Y, %H:%M:%S")),
            'condition': self.condition,
            'value': self.value
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_pending(cls):
        return cls.query.filter_by(sended=False).firts()

    @classmethod
    def find_by_entity(cls, nameEntity):
        return cls.query.filter_by(entity=nameEntity).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
