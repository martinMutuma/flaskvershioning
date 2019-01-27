import werkzeug.exceptions as ex
from app.models import User
from flask_restful import Resource
from flask import request, jsonify, make_response, abort, Response
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from app import app
import datetime
import functools

def authorize():

            # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
                my_auth = Auth()
                payload = my_auth.decode_auth_token(auth_token)

                if payload != False:

                    return payload
                else:
                    return abort(401,"Invalid Token")
            except IndexError:
                return abort(401,"Invalid Token")

class Auth(Resource):
    def create_auth_token(self, user):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'name': user.username,
                'email': user.email,
            }
            return jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256').decode()
        except Exception:
            return False

    def decode_auth_token(self, auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: List
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload
        except jwt.InvalidTokenError:
            return False

    def checkLogin(self):

            # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
                payload = self.decode_auth_token(auth_token)

                if payload != False:

                    return payload
                else:
                    return abort(401,"Invalid Token")
            except IndexError:
                return abort(401,"Invalid Token")

class Signup(Auth):
    def post(self):
        '''Add new user'''

        post_data = request.form
        username = post_data['username']
        email = post_data['email']
        password = post_data['password']

        if not email:
            return {"message": "Email Required", }, 404

        # imprement data validation

        new_user = User(username=username, email=email, password=password)
        if new_user.save():
            token = self.create_auth_token(new_user)
            return {
                "message": "account created successfully",
                "token": token,
                "user": new_user.serialize()}, 201
        else:
            return {"message": "Encountared a problem creating user"}, 404


class Login(Auth):

    def post(self):
        post_data = request.form
        email = post_data['email']
        password = post_data['password']

        if not email or not password:
            return {'message': "Please supply login creadentials"}, 404

        user = User.query.filter_by(email=email).first()
        if not (user.check_password(password)):
            return {'message': "Invalid login credentials"}, 404
        else:
            token = self.create_auth_token(user)
            return {'message': "login succesful", 'token': token}, 200


