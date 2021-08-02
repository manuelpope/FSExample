from flask_restful import Resource

from server_Flask.server.models.Sales import SalesModel


class SeriesTime(Resource):

    @classmethod
    def get(self):
        sales = [item.json() for item in SalesModel.find_all()]

        return {'items': sales}, 200
