from flask_restful import Resource

from server_Flask.server.models.Stores import StoreModel


class StoresInfo(Resource):

    @classmethod
    def get(self):
        stores = [item.json() for item in StoreModel.find_all()]

        return {'sucursales': stores}, 200
