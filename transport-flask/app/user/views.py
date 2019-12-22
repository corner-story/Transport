from app.user import user
from flask import request, jsonify
from app.models import Consigner
from app.models import Driver
from app.extensions import db
from app.utils import login_required
import pysnooper


#货主的信息
@user.route("/consigner/")
@login_required
def consigner_info():
    res={
         "state": "success", "msg": "get consigner information successfully", "data": {}
    }
    
    consigner_id = request.args.get("id")
    if(consigner_id == None):
        res["state"] = "error"
        res["msg"] = "error id: None"
        return jsonify(res)
    try:
        consigner = Consigner.query.filter_by(id=consigner_id).first()
    except Exception as e:
        res["state"] = "error"
        res["msg"] = str(e)
        return jsonify(res)

    data = {
        "id": consigner.id,
        "username": consigner.username,
        "password_hash": consigner.password_hash,
        "phone_number": consigner.phone_number,
        "email": consigner.email,
        "general_good": consigner.general_good,
        "address": consigner.address,
        "account": consigner.account,
        "user_type": consigner.user_type,
        "backup": consigner.backup,
        "timestamp":consigner.timestamp
    }

    res["data"] = data
    return jsonify(res)

#司机的信息
@user.route("/driver/")
@login_required
def driver_info():
    res={
         "state": "success", "msg": "get driver information successfully", "data": {}
    }

    driver_id = request.args.get("id")
    if(driver_id == None):
        res["state"] = "error"
        res["msg"] = "error id: None"
        return jsonify(res)
    try:
        driver = Consigner.query.filter_by(id=driver_id).first()
    except Exception as e:
        res["state"] = "error"
        res["msg"] = str(e)
        return jsonify(res)

    data = {
        "id": driver.id,
        "username": driver.username,
        "password_hash": driver.password_hash,
        "phone_number": driver.phone_number,
        "email": driver.email,
        "car_type": driver.car_type,
        "car_number": driver.car_number,
        "transport_type": driver.transport_type,
        "account": driver.account,
        "user_type": driver.user_type,
        "backup": driver.backup,
        "timestamp":driver.timestamp
    }

    res["data"] = data
    return jsonify(res)