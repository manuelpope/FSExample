
from Factory import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    mail = db.Column(db.String(80))
    country = db.Column(db.String(80))


    def __init__(self, username, password, mail, country):
        self.username = username
        self.password = password
        self.mail = mail
        self.country = country

    def json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        print(user)
        if user:
            return user
        return None

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    @classmethod
    def find_by_mail(cls, _mail):
        user = cls.query.filter_by(mail=_mail).first()
        if user:
            return user
        return None
