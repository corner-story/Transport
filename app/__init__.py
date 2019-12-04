from flask import Flask, session, url_for, redirect, request, render_template, jsonify
from app.extensions import db, migrate
from app.model import Driver, Consigner, Good, Application
from app import config
from app.utils import login_required
import pysnooper
import os

app = Flask(__name__)

basedir = os.path.abspath('.')
logdir = os.path.abspath("./log")

app.config.from_object(config)
db.init_app(app=app)
migrate.init_app(app=app, db=db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/", methods=["GET", "POST"])
@pysnooper.snoop(output=f"{logdir}/login.log")
def login():
    if(request.method == "POST"):
        data = {
            "code": "200"
            ,"msg": "登录成功!"
            ,"url": "/index/"
        }
        
        phone = request.form.get("phone")
        password = request.form.get("password")

        user = Driver.query.filter_by(phone_number = phone).first() 
        if user is None:
            user = Consigner.query.filter_by(phone_number = phone).first()

        islogin = False
        if user and user.check_password(password):
            islogin = True
            session["islogin"] = islogin
            session["role"] = user.user_type
            session["username"] = user.username
            data["msg"] = f"登陆成功, 你的角色为{session['role']}!"
        else:
            data["msg"] = "登录失败"
        return jsonify(data)
    return render_template("login.html")


@app.route("/register/")
def register():
    return render_template("register.html")

