from flask_restful import Resource, reqparse

from models.Sales import SalesModel

from service.validator import Validator_Sale


_parser_request_sale = reqparse.RequestParser()
_parser_request_sale.add_argument('month',
                                  type=int,
                                  required=True,
                                  help="This field cannot be blank."
                                  )
_parser_request_sale.add_argument('price',
                                  type=float,
                                  required=True,
                                  help="This field cannot be blank."
                                  )
_parser_request_sale.add_argument('store_id',
                                  type=int,
                                  required=True,
                                  help="This field cannot be blank."
                                  )



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
    @classmethod
    def post (self):
        data = _parser_request_sale.parse_args()
        sale = SalesModel(**data)
        sale.save_to_db()
        list_condition_id = Validator_Sale.validate_condition('sales','price',sale.price)
        if len(list_condition_id)>0:
            print("logic to populate table task pending mail"+str(list_condition_id))
        return {'sale': sale.json()},200



class SeriesTime(Resource):

    @classmethod
    def get(self):
        sales = [item.json() for item in SalesModel.find_all()]

        return {'items': sales}, 200
