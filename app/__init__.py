from flask import Flask, session, url_for, redirect, request, render_template
from app.extensions import db, migrate
from app.model import Driver, Consigner, Good, Application
from app import config
from app.utils import login_required

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app=app)
migrate.init_app(app=app, db=db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    return "login!"