
from flask import Flask

app = Flask(__name__)

from app.v1.routes import mod



app.register_blueprint(mod, url_prefix='/v1')
# app.register_blueprint(v2.routes.mod2, url_prefix='v2')
