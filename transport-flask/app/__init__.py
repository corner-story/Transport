from flask import Flask, jsonify
from app.extensions import db, migrate
from flask_cors import CORS
from app import config
from app.auth import auth
from app.user import user
from app.good import good


app = Flask(__name__)
app.config.from_object(config)


# 插件
db.init_app(app=app)
migrate.init_app(app=app, db=db)

# cors
CORS(app=app, supports_credentials=True)

# 蓝图
app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(user, url_prefix="/api")
app.register_blueprint(good, url_prefix="/api")


# login_required
from app.utils import login_required

# 命令行工具
from app.commands import rebuild, forge, forge1





