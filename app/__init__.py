
from app.v2.routes import mod2
from app.v1.routes import mod

from flask import Flask

app = Flask(__name__)

#The above should be here but my auto formartter keeps sending them up there
#from app.v2.routes import mod2
#from app.v1.routes import mod
app.register_blueprint(mod, url_prefix='/api/v1')
app.register_blueprint(mod2, url_prefix='/api/v2')
