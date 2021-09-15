import requests
from flask_restful import Resource

from models.Stores import StoreModel


class StoresInfo(Resource):

    @classmethod
    def get(self):
        stores = [item.json() for item in StoreModel.find_all()]

        return {'sucursales': stores}, 200


class StoresResume(Resource):

    @classmethod
    def get(self):
        stores = [item.json() for item in StoreModel.find_all()]
        infoAbstract = {}

        for store in stores:
            infoSalesMonth = {}
            quantityPerMonth = {}
            for m in range(1, 13):
                infoSalesMonth[m] = 0
                quantityPerMonth[m] = 0

            [accumulate(infoSalesMonth, elem) for elem in store['items']]
            [accumulateQuantity(quantityPerMonth, elem) for elem in store['items']]

            infoAbstract[store['id']] = {

                'salesMonthly': infoSalesMonth,
                'quantityMonthly': quantityPerMonth,
                'name': store['name'],
                'telf': store['telf'],
                'address': store['address']
            }

        return {'sucursales': infoAbstract}, 200


def accumulate(dictMonths, elem):
    dictMonths[elem['month']] = round(dictMonths[elem['month']] + elem['price'], 0)
    return dictMonths


def accumulateQuantity(dictMonths, elem):
    dictMonths[elem['month']] = round(dictMonths[elem['month']] + 1, 0)
    return dictMonths


class RemoteApi(Resource):

    @classmethod
    def get(self):
        r = requests.get('https://www.xm.com.co/despachonacional/2021-08/dDEC0818_NAL.TXT', verify=False,
                         allow_redirects=True)

        r = r.text.split("\r\n")
        r = [elem.replace('\"', "") for elem in r]

        return {'data': r}, 200
