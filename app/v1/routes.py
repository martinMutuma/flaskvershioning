from flask import Blueprint, url_for
from flask import jsonify
mod = Blueprint('api_v1', __name__)


@mod.route('/')
def list_routes():
    # """"List all routes in this version of the app""""

    routes = []
    from flask import Flask
    mod_temp_app = Flask(__name__)
    mod_temp_app.register_blueprint(mod)
    for route in mod_temp_app.url_map.iter_rules():
        routes.append(str(route))
    return jsonify(routes)


@mod.route('/test')
def test():
    return ('This is version 1 of the test route')
