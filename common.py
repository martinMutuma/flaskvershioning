#mainpath/common.py
#file Used to run the app
from app import app, db


if __name__ == "__main__":
    app.run(debug=True)
