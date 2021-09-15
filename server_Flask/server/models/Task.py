from datetime import datetime

from db import db


class TaskModel(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80))
    condition_id = db.Column(db.String(80))
    sended_mail = db.Column(db.Boolean, default=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, subject, condition_id, sended_mail=0):
        self.subject = subject
        self.condition_id = condition_id
        self.sended_mail = sended_mail

    def json(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'sended_mail': self.sended_mail,
            'time_stamp': str(self.time_stamp.strftime("%m/%d/%Y, %H:%M:%S")),
            'condition_id': self.condition_id
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_pending(cls):
        return cls.query.filter_by(sended_mail=False).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
