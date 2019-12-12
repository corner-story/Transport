from flask_restful import Resource
from app.models import Driver, Consigner, Good, Application
from app import api
from flask import request, Response, jsonify, session, make_response
from app.extensions import db

class Login(Resource):
    def post(self):
        json = request.get_json()
        phone = json.get("phone")
        password = json.get("password")

        user = Driver.query.filter_by(phone_number = phone).first() 
        if user is None:
            user = Consigner.query.filter_by(phone_number = phone).first()

        data = {
            "state": "success"
            ,"msg": ""
        }
        res = None
        if user and user.check_password(password):
            # 登录成功
            data["msg"] = "登录成功!"

            # 记录session
            session["islogin"] = True
            session["role"] = user.user_type
            session["username"] = user.username
            
            res = jsonify(data)
            # 设置客户端cookie
            res.set_cookie("islogin", "true", httponly=False)
            res.set_cookie("role", user.user_type, httponly=False)
            res.set_cookie("username", user.username, httponly=False)
            res.set_cookie("userid", str(user.id), httponly=False)  # 把id转化为str类型
  
        else:
            data["state"] = "error"
            data["msg"] = "登录失败, 请检查手机号和密码是否正确!"
            res = jsonify(data)
        
        return res


class Register(Resource):

    def post(self):
        json = request.get_json()
        username = json.get("username")
        phone = json.get("phone")
        password = json.get("password")
        role = json.get("role")

        data = {
            "state": "success",
            "msg": "注册成功",
            "data": {}
        }

        # 先检测该phone是否已经注册
        user = Driver.query.filter_by(phone_number = phone).first()
        if user is None:
            user = Consigner.query.filter_by(phone_number = phone).first()
        if user is not None:
            data["state"] = "error"
            data["msg"] = "该手机号码已经被注册了哦!"
            return jsonify(data)
        
        # 注册该用户
        if role == "1":
            user = Driver(username=username, phone_number=phone, password=password)
        else:
            user = Consigner(username=username, phone_number=phone, password=password)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            data["state"] = "error"
            data["msg"] = str(e)
        
        return jsonify(data)






api.add_resource(Login, "/api/login")
api.add_resource(Register, "/api/register")