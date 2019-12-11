from flask_restful import Resource
from app.models import Driver, Consigner, Good, Application
from flask import request, jsonify 
from app import api

class Login(Resource):

    def post(self):
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


api.add_resource(Login, "/login")