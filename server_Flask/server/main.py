import numpy as np
from apscheduler.scheduler import Scheduler
from flask import Flask
from flask_restful import Api

from db import db
from models.Sales import SalesModel
from models.Stores import StoreModel
from resources.DataSales import SeriesTime, SeriesTimeResume
from resources.DataStore import StoresInfo, StoresResume, RemoteApi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
scheduler = Scheduler()
scheduler.start()


# @app.before_first_request
def create_tables():
    db.create_all()
    storeA = StoreModel('Sucursal 1', '1420 av Clinton', 121312)
    storeB = StoreModel('Sucursal 2', '1000 cll Emily', 324323)
    storeB.save_to_db()
    storeA.save_to_db()

    populate_sales(1)
    populate_sales(2)


def populate_sales(idStore):
    for month in range(1, 13):
        total = np.random.randint(1, 200)
        for _ in range(total):
            mockSale = SalesModel(month, round(np.abs(np.random.uniform(0, 200)), 2), idStore)
            mockSale.save_to_db()


@app.route("/")
def status():
    return {'message': 'running status ok - green'}, 200

@scheduler.interval_schedule(minutes=1, misfire_grace_time=10)
def job_function():
   print("this is the function reviewing table of tasks")


api.add_resource(SeriesTime, '/series')
api.add_resource(SeriesTimeResume, '/seriesresume')
api.add_resource(StoresInfo, '/stores')
api.add_resource(StoresResume, '/storesresume')
api.add_resource(RemoteApi, '/remote')

db.init_app(app)
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=3001, debug=True, threaded=True)
