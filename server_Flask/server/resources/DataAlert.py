from flask_restful import Resource, reqparse

from models.Alert import AlertModel

_parser_reuest_alert = reqparse.RequestParser()
_parser_reuest_alert.add_argument('entity',
                                  type=str,
                                  required=True,
                                  help="This field cannot be blank."
                                  )
_parser_reuest_alert.add_argument('value',
                                  type=float,
                                  required=True,
                                  help="This field cannot be blank."
                                  )
_parser_reuest_alert.add_argument('field',
                                  type=str,
                                  required=True,
                                  help="This field cannot be blank."
                                  )
_parser_reuest_alert.add_argument('condition',
                                  type=str,
                                  required=True,
                                  help="This field cannot be blank."
                                  )


class ControllerAlert(Resource):

    @classmethod
    def get(self):
        alerts = [item.json() for item in AlertModel.find_all()]

        return {'alerts': alerts}, 200


class ControllerPushData(Resource):

    def post(self):
        data = _parser_reuest_alert.parse_args()
        if not data.get('condition') in ['greater', 'equal', 'lesser']:
            return {'message': "not proper condition like 'greater','equal','lesser'"}, 400

        alert = AlertModel(**data)
        alert.save_to_db()

        return {'alert': alert.json()}, 200
