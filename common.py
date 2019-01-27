#mainpath/common.py
#file Used to run the app
from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    app.run(debug=True)
