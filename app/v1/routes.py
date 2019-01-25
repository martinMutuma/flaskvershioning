from app.v1.auth import Signup
from flask import Blueprint, url_for
from flask import jsonify
from flask_restful import Resource, Api

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
    def get(self):
        return {"message": "This is test url"}, 200


modApi = Api(mod)
modApi.add_resource(DefaultRoutes, '/')
modApi.add_resource(Signup, '/signup')
modApi.add_resource(Test, '/test')
