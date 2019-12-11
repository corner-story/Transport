from flask import Flask, jsonify, render_template
from app.extensions import db, migrate
from app.models import Driver, Consigner, Good, Application
from flask_cors import CORS
from flask_restful import Resource, Api
from app import config

app = Flask(__name__)
app.config.from_object(config)

# 插件
db.init_app(app=app)
migrate.init_app(app=app, db=db)

# cors
CORS(app=app)

# restful
api = Api(app)


class Hello(Resource):
    def get(self):
        drivers = Driver.query.all()
        res = [{"username": driver.username, "phone_number": driver.phone_number} for driver in drivers]
        return jsonify(res)


api.add_resource(Hello, "/")


# auth api
from app.auth import *

# 命令行工具
from app.commands import rebuild, forge


