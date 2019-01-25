from flask import Blueprint, url_for
from flask import jsonify
mod2 = Blueprint('api_v2', __name__)


@mod2.route('/')
def list_routes():
    #""""List all routes in this version of the app""""
    routes = []
    from flask import Flask
    mod_temp_app = Flask(__name__)
    mod_temp_app.register_blueprint(mod2)
    for route in mod_temp_app.url_map.iter_rules():
        routes.append(str(route))
    return jsonify(routes)

#


@mod2.route('/test')
def test():
    return ('<h1>This is version 2 of the test route</h1>')
