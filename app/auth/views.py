from app.auth import auth
from flask import redirect, render_template, request, jsonify
from app.model import Driver, Consigner, Good, Application

@auth.route("/")
def index():
    return render_template("auth/index.html")


@auth.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")

    if(request.method == "POST"):
        phone = request.form.get("phone")
        password = request.form.get("password")

        user = Driver.query.filter_by(phone_number = phone).first() 
        if user is None:
            user = Consigner.query.filter_by(phone_number = phone).first()

        data = {
            "code": "200"
            ,"msg": ""
            ,"url": "#"
        }
        if user and user.check_password(password):
            # 登录成功
            session["islogin"] = True
            session["role"] = user.user_type
            session["username"] = user.username
            
            data["msg"] = "登录成功!"
            data["url"] = "/"
        else:
            data["msg"] = "登录失败, 请检查手机号和密码是否正确!"
        return jsonify(data)
    


@auth.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/register.html")
    if request.method == "POST":
        pass

