from flask import Blueprint

auth = Blueprint("auth", __name__)

# 避免循环导入
# 注册前端页面
from app.auth import views
from app.auth import errors