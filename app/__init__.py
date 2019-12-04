from flask import Flask
from app.extensions import db, migrate
from app.model import Driver, Consigner, Good, Application
from app import config

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app=app)
migrate.init_app(app=app, db=db)

@app.route("/")
def index():
    return "Hello, flask!"
