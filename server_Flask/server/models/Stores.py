from Factory import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    address = db.Column(db.String(80))
    telf = db.Column(db.Integer)

    items = db.relationship('SalesModel', lazy='dynamic')

    def __init__(self, name, address, telf):
        self.name = name
        self.address = address
        self.telf = telf

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'telf': self.telf,
            'items': [item.json() for item in self.items.all()]
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
