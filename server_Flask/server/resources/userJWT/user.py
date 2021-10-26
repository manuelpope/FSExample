import logging
import re

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash

from blacklist import BLACKLIST
from models.user import UserModel

_user_parser_restore = reqparse.RequestParser()
_user_parser_restore.add_argument('username',
                                  type=str,
                                  required=True,
                                  help="This field cannot be blank."
                                  )
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('mail',
                          type=str,
                          required=False,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('country',
                          type=str,
                          required=False,
                          help="This field optional"
                          )
logger = logging.getLogger()

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        error = self.validation_request(data)
        if error:
            return error

        user = UserModel(**data)

        user.password = generate_password_hash(data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201

    def validation_request(self, data):

        if UserModel.find_by_username(data['username']):
            return {"message": "A userJWT with that username already exists"}, 400

        if not data['mail']:
            return {"message": "mail could not be blank"}, 400
        elif not re.match(regex, data['mail']) or UserModel.find_by_mail(data['mail']):
            return {"message": "its not a valid mail or its already exist that mail"}, 400


class User(Resource):
    """
    This resource can be useful when testing our Flask app. We may not want to expose it to public users, but for the
    sake of demonstration in this course, it can be useful when we are manipulating data regarding the users.
    """

    @classmethod
    def get(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        return user.json(), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message': 'User Not Found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted.'}, 200


class UserLogin(Resource):
    def post(self):
        logger.info("identify userJWT")
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data['username'])
        print(user.json())
        # this is what the `authenticate()` function did in security.py
        if user and check_password_hash(user.password, data['password']):
            # identity= is what the identity() function did in security.py—now stored in the JWT
            access_token = create_access_token(identity=user.username, fresh=True)
            refresh_token = create_refresh_token(user.username)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token
                   }, 200

        return {"message": "Invalid Credentials!"}, 401


class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        BLACKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200


class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """
        Get a new access token without requiring username and password—only the 'refresh token'
        provided in the /login endpoint.

        Note that refreshed access tokens have a `fresh=False`, which means that the userJWT may have not
        given us their username and password for potentially a long time (if the token has been
        refreshed many times over).
        """
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200


class UpdatePass(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('password',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
                            )

        data = parser.parse_args()
        current_user = get_jwt_identity()
        user = UserModel.find_by_username(current_user)
        if get_jwt()['resetPass'] and user and not check_password_hash(user.password, data['password']):
            
            user.password = generate_password_hash(data['password'])
            user.update_to_db()
            return {'message': 'password has been changed successfully'}, 200

        return {'message': 'password its no a valid one'}, 400
