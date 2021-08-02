from flask_restful import Resource

from models.Sales import SalesModel


class SeriesTimeResume(Resource):

    @classmethod
    def get(self):
        sales = [item.json() for item in SalesModel.find_all()]
        amountPerMonth = {}
        quantityPerMonth = {}
        for m in range(1, 13):
            amountPerMonth[m] = 0
            quantityPerMonth[m] = 0

        for sale in sales:
            amountPerMonth[sale['month']] = round(amountPerMonth[sale['month']] + sale['price'], 0)
            quantityPerMonth[sale['month']] = quantityPerMonth[sale['month']] + 1

        sales = {
            'amountPerMonthAllStores': amountPerMonth,
            'quantityPerMonthAllStores': quantityPerMonth
        }

        return {'items': sales}, 200


class SeriesTime(Resource):

    @classmethod
    def get(self):
        sales = [item.json() for item in SalesModel.find_all()]

        return {'items': sales}, 200
