from datetime import datetime

import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_restful import Api

from db import db
from models.Alert import AlertModel
from models.Sales import SalesModel
from models.Stores import StoreModel
from models.Task import TaskModel
from resources.DataAlert import ControllerAlert, ControllerPushData
from resources.DataSales import SeriesTime, SeriesTimeResume
from resources.DataStore import StoresInfo, StoresResume, RemoteApi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)
sched = BackgroundScheduler()


# @app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()
    storeA = StoreModel('Sucursal 1', '1420 av Clinton', 121312)
    storeB = StoreModel('Sucursal 2', '1000 cll Emily', 324323)
    storeB.save_to_db()
    storeA.save_to_db()

    populate_sales(1)
    populate_sales(2)
    alertTest = AlertModel(entity="sales", value=124.45, field="price", condition='greater')
    alertTest.save_to_db()


def populate_sales(idStore):
    for month in range(1, 13):
        total = np.random.randint(1, 200)
        for _ in range(total):
            mockSale = SalesModel(month, round(np.abs(np.random.uniform(0, 200)), 2), idStore)
            mockSale.save_to_db()


@app.route("/")
def status():
    return {'message': 'running status ok - green'}, 200


@sched.scheduled_job('interval', id='my_job_id', seconds=60)
def job_function():
    print("this is the function reviewing table of tasks   at :: " + str(datetime.now()))
    with app.app_context():
        list_task = TaskModel.find_pending()
        if list_task:
            print("processing sending mail alert", len(list_task))
            print("changing sent flag status")
            for task in list_task:
                task.sended_mail = 1
                task.save_to_db()


# enable to start scheduling tasks
sched.start()

api.add_resource(SeriesTime, '/series')
api.add_resource(SeriesTimeResume, '/seriesresume')
api.add_resource(StoresInfo, '/stores')
api.add_resource(StoresResume, '/storesresume')
api.add_resource(RemoteApi, '/remote')
api.add_resource(ControllerAlert, '/getalerts')
api.add_resource(ControllerPushData, '/postalert')

db.init_app(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True, threaded=True)
