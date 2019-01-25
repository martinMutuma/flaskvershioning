from app.models import User
from flask_restful import Resource
from flask import request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash


class Signup(Resource):
    def post(self):
        '''Add new user'''

        post_data = request.form
        username = post_data['username']
        email = post_data['email']
        password = post_data['password']

        if not email:
            return {"message": "account created successfully", }, 404

        # imprement data validation

        new_user = User(username=username, email=email, password=password)
        if new_user.save():
            return {
                "message": "account created successfully",
                "user": new_user.serialize()}, 201
        else:
            return {"message": "Encountared a problem creating user"}, 404
