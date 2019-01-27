from app.v1.auth import Signup, Login
from flask import Blueprint, url_for
from flask import jsonify
from flask_restful import Resource, Api
from app.v1.auth import  authorize

mod = Blueprint('api_v1', __name__)


class DefaultRoutes(Resource):
    def get(self):
        """List all routes in this version of the app"""

        routes = []
        from flask import Flask
        mod_temp_app = Flask(__name__)
        mod_temp_app.register_blueprint(mod)
        for route in mod_temp_app.url_map.iter_rules():
            routes.append(str(route))
        return jsonify(routes)


class Test(Resource):
    # @checkLogin
    def get(self):
        authorize()
        return {"message": "This is test url"}, 200


modApi = Api(mod)
modApi.add_resource(DefaultRoutes, '/')
modApi.add_resource(Signup, '/auth/signup')
modApi.add_resource(Login, '/auth/login')

modApi.add_resource(Test, '/test')

