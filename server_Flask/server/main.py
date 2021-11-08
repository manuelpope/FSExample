from datetime import datetime

import numpy as np
import json
from flask import Flask,Response,jsonify
import requests
from flask_restful import Api,Resource
import queue

from Factory import db,sched,announcer
from models.Alert import AlertModel
from models.Sales import SalesModel
from models.Stores import StoreModel
from models.Task import TaskModel
from resources.DataAlert import ControllerAlert, ControllerPushData
from resources.DataSales import SeriesTime, SeriesTimeResume
from resources.DataStore import StoresInfo, StoresResume, RemoteApi
from resources.userJWT.user import UserLogin, UserLogout, UserRegister, TokenRefresh, UpdatePass, \
    _user_parser_restore
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from blacklist import BLACKLIST
from models.user import UserModel



################################################### Global objects######################################
##########TODO CARGAR DESDE ARCHIVO DE CONFIGURACIÓN
with open('appConfig.json') as f:
    dataConfig = json.load(f)
for config in dataConfig.values():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']
    app.config['PROPAGATE_EXCEPTIONS'] = config['PROPAGATE_EXCEPTIONS']
    app.config['JWT_BLACKLIST_ENABLED'] = config['JWT_BLACKLIST_ENABLED'] # enable blacklist feature
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = config['JWT_BLACKLIST_TOKEN_CHECKS']  # allow blacklisting for access and refresh tokens
    app.secret_key = config['secret_key'] # could do app.config['JWT_SECRET_KEY'] if we prefer
    api = Api(app)
    jwt = JWTManager(app)
    q = queue.Queue()

    TOKEN = config['TOKEN']
    CHAT_ID = config['CHAT_ID']

########################## Controller mapping  without classes ###########################################

def bot_send_text(bot_message):
    bot_token = TOKEN
    bot_chatID = CHAT_ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    print(send_text)
    response = requests.get(send_text)

    return response

#@app.before_first_request
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

@sched.scheduled_job('interval', id='my_job_id', seconds=30)
def job_function():
    print("this is the function reviewing table of tasks   at :: " + str(datetime.now()))
    with app.app_context():
        list_task = TaskModel.find_pending()
        if list_task:

            msg = f'data: {"refresh"}\n\n'
            announcer.announce(msg=msg)


            print("processing sending mail alert", len(list_task))
            print("changing sent flag status")
            for task in list_task:
                r = bot_send_text(str(task.json()))
                print(r)
                task.sended_mail = 1
                task.save_to_db()

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    # "MAIL_USERNAME": os.environ['username'],
    # "MAIL_PASSWORD": os.environ['******']
    "MAIL_USERNAME": '*****',
    "MAIL_PASSWORD": '******'
}

def worker():
    # Aqui va el envio de correos o alguna tarea muy pesada que se encola/ como correos.
    n = 1
    while n > 0:
        item = q.get()
        # print(f'Working on {item}', q.qsize())
        send_mail(item)
        q.task_done()
        n = q.qsize()


def send_mail(dictMail):
    with app.app_context():
        mail_settings, mail, msg = dictMail['mail_settings'], dictMail['mail'], dictMail
        message = Message(subject=msg['subject'],
                          sender=mail_settings["MAIL_USERNAME"],
                          recipients=[msg['recipients']],  # use your email for testing
                          body=msg['body'],
                          html=msg['html'])
        mail.send(message=message)


@app.route('/listen', methods=['GET'])
def listen():

    def stream():

        messages = announcer.listen()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            print('\n'+msg)
            yield msg

    return Response(stream(), mimetype='text/event-stream',headers={
        'Access-Control-Allow-Origin': '*',
        'transfer-enconding':'chunked','Connection': 'Keep-Alive',
        'Keep-Alive': 'timeout=5, max = 1000'})





"""
`claims` are data we choose to attach to each jwt payload
and for each jwt protected endpoint, we can retrieve these claims via `get_jwt_claims()`
one possible use case for claims are access level control, which is shown below.
"""


@jwt.additional_claims_loader
def add_claims_to_access_token(identity):  # Remember identity is what we define when creating the access token
    if identity == 1:  # instead of hard-coding, we should read from a config file or database to get a list of admins instead
        return {'is_admin': True}
    return {'is_admin': False}


# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in BLACKLIST  # Here we blacklist particular JWTs that have been created in the past.


# The following callbacks are used for customizing jwt response/error messages.
# The original ones may not be in a very pretty format (opinionated)
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        'error': 'authorization_required'
    }), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify({
        "description": "The token is not fresh.",
        'error': 'fresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({
        "description": "The token has been revoked.",
        'error': 'token_revoked'
    }), 401
class RestorePass(Resource):
    def post(self):
        data = _user_parser_restore.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            new_token = create_access_token(identity=user['username'],
                                            expires_delta=datetime.timedelta(seconds=1800),
                                            additional_claims={"resetPass": True})
            # Here logic to send the mail with delta token...
            nameuser = user['username']
            dictMail = {"subject": "reset your password BRAI",
                        'sender': mail_settings["MAIL_USERNAME"],
                        'recipients': user['mail'],
                        'body': f'{nameuser}To  reset  your password pls use the token in the webpage ' + new_token,
                        'mail_settings': mail_settings,
                        'mail': mail,
                        'html': '<p>' + nameuser +
                                '  To  reset  your password ,from  <strong>BRAI</strong></p>' +
                                '<p>  TOKEN: ' +
                                '<strong>' + new_token + '</strong></p>'
                        }
            Thread(target=worker, daemon=True).start()
            q.put(dictMail)
            return {'access_token': new_token,
                    'message': 'Reset token has been sent, please this only last for 30 min'}, 200
        return {"message": "Invalid Username !"}, 401


############################## controllers from classes crud Resources ####################################


api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(UserLogout, '/logout')
api.add_resource(UserRegister, '/register')
api.add_resource(RestorePass, '/resetpass')
api.add_resource(UpdatePass, '/updatepass')

api.add_resource(SeriesTime, '/series')
api.add_resource(SeriesTimeResume, '/seriesresume')
api.add_resource(StoresInfo, '/stores')
api.add_resource(StoresResume, '/storesresume')
api.add_resource(RemoteApi, '/remote')
api.add_resource(ControllerAlert, '/getalerts')
api.add_resource(ControllerPushData, '/postalert')



# enable to start scheduling tasks & DataBase


sched.start()
db.init_app(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True, threaded=True)
