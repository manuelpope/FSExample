import numpy as np
from flask import Flask
from flask_restful import Api

from db import db
from models.Sales import SalesModel
from models.Stores import StoreModel
from resources.DataSales import SeriesTime, SeriesTimeResume
from resources.DataStore import StoresInfo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


#@app.before_first_request
def create_tables():
    db.create_all()
    storeA = StoreModel('Sucursal 1', '1420 av Clinton')
    storeB = StoreModel('Sucursal 2', '1000 cll Emily')
    storeB.save_to_db()
    storeA.save_to_db()

    populate_sales(1)
    populate_sales(2)


def populate_sales(idStore):
    for month in range(1, 13):
        total = np.random.randint(1, 200)
        for _ in range(total):
            mockSale = SalesModel(month, round(np.abs(np.random.uniform(0, 200)),2), idStore)
            mockSale.save_to_db()


@app.route("/")
def status():
    return {'message': 'running status ok - green'}, 200


api.add_resource(SeriesTime, '/series')
api.add_resource(SeriesTimeResume, '/seriesresume')
api.add_resource(StoresInfo, '/stores')

if __name__ == "__main__":
    db.init_app(app)
    app.run(host="0.0.0.0", port=3001, debug=True, threaded=True)
