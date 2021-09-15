from Factory import db


class SalesModel(db.Model):
    __tablename__ = 'sale'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, month, price, store_id):
        self.month = month
        self.price = price
        self.store_id = store_id

    def json(self):
        return {
            'id': self.id,
            'month': self.month,
            'price': self.price,
            'store_id': self.store_id
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
