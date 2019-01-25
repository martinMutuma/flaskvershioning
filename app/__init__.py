

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)
migrations = Migrate(app, db)
from app.models import *
from app.v2.routes import mod2
from app.v1.routes import mod
# The above should be here but my auto formartter keeps sending them up there
#from app.v2.routes import mod2
#from app.v1.routes import mod

app.register_blueprint(mod, url_prefix='/api/v1')
app.register_blueprint(mod2, url_prefix='/api/v2')