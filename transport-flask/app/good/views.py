from app.good import good
from flask import request, jsonify, session
from app.models import Good, Application, GoodType
from app.extensions import db
from app.utils import login_required, next_status
from sqlalchemy import and_
import pysnooper


# 获取所有可利用的，即处于"等待司机承运"状态的货物
@good.route("/goods/")
@login_required
def get_available_goods():
    res = {
        "state": "success", "msg": "get available goods successfully", "data": []
    }
    page = request.args.get("page")
    limit = request.args.get("limit")

    if(page == None or limit == None):
        res["state"] = "error"
        res["msg"] = "you must give me 'page' and 'limit'!"
        return jsonify(res)

    page = int(page)
    limit = int(limit)

    goods = Good.query.filter_by(isactive=1).order_by(
        Good.timestamp.desc()).paginate(page, limit, error_out=False)

    goods = [
        {
            "id": good.id,
            "good_name": good.good_name,
            "transport_origin": good.transport_origin,
            "transport_des": good.transport_des,
            "transport_money": good.transport_money,
            "transport_time": good.transport_time,
            "username": good.consigner.username,
            "consigner_id": good.consigner.id
        }
        for good in goods.items
    ]
    res["data"] = goods

    return jsonify(res)


@good.route("/good/")
@login_required
def get_one_good():
    res = {
        "state": "success", "msg": "get good successfully", "data": []
    }
    good_id = request.args.get("id")
    # 查找对应的货物
    good = Good.query.filter_by(id=good_id).first()

    if(good == None):
        res["state"] = "error"
        res["msg"] = "error"
        return jsonify(res)

    data = {
        "id": good.id,
        "good_name": good.good_name,
        "transport_origin": good.transport_origin,
        "transport_des": good.transport_des,
        "transport_money": good.transport_money,
        "backup": good.backup,
        "consigner": good.consigner.username,
        "consigner_id": good.consigner.id,
        "phone_number": good.consigner.phone_number
    }

    res["data"] = data
    return jsonify(res)


# 申请货物
@good.route("/application/", methods=["POST"])
@login_required
def send_application():
    res = {
        "state": "success", "msg": "send applicaton successfully", "data": []
    }
    request_data = request.get_json()
    driver_id = session.get("id")
    good_id = request_data.get("good_id")

    if driver_id == None or good_id == None:
        res["state"] = "error"
        res["msg"] = "fuck you!"
        return jsonify(res)

    application = Application(driver_id=driver_id, good_id=good_id)

    try:
        db.session.add(application)
        db.session.commit()
    except Exception as e:
        data["state"] = "error"
        data["msg"] = str(e)

    return jsonify(res)


# 货主查看所有对自己货物的申请
@good.route("/applications/")
@login_required
def get_available_applications():
    res = {
        "state": "success", "msg": "get applicatons successfully", "data": []
    }
    if session.get("role", None) == None or session.get("role") != "consigner":
        res["state"] = "error"
        res["msg"] = "fuck you!"
        return jsonify(res)
    consigner_id = session.get("id")
    goods = Good.query.filter(and_(Good.consigner_id == consigner_id,
                                   Good.isactive == 1)).order_by(Good.timestamp.desc()).all()
    goods = [good.id for good in goods]

    applications = Application.query.filter(and_(Application.good_id.in_(
        goods), Application.result == "等待审核")).order_by(Application.timestamp.desc()).all()

    data = [
        {
            "id": application.id,
            "result": application.result,
            "backup": application.backup,
            "timestamp": application.timestamp,
            "driver_name": application.driver.username,
            "driver_phone": application.driver.phone_number,
            "good_name": application.good.good_name
        }
        for application in applications
    ]

    res["data"] = data
    return jsonify(res)


@good.route("/isagree/", methods=["POST"])
def change_application_state():
    res = {
        "state": "success", "msg": "set applicaton-state successfully", "data": []
    }
    request_data = request.get_json()
    application_id = request_data.get("id")
    isagree = request_data.get("state")

    application = Application.query.get(application_id)
    application.result = isagree
    if application.result == "同意":
        application.good_status = "选定司机"

    db.session.add(application)
    db.session.commit()

    return jsonify(res)


@good.route("/goods/agreed")
@login_required
def get_agreed_applications():
    res = {
        "state": "success", "msg": "get applicatons successfully", "data": []
    }
    if session.get("role", None) == None or session.get("role") != "consigner":
        res["state"] = "error"
        res["msg"] = "fuck you!"
        return jsonify(res)

    consigner_id = session.get("id")
    # applications = Application.query.filter(and_(Application.good.consigner.id == consigner_id, Application.result=="同意")).order_by(Application.timestamp.desc()).all()

    goods = Good.query.filter(and_(Good.consigner_id == consigner_id,
                                   Good.isactive == 1)).order_by(Good.timestamp.desc()).all()
    goods = [good.id for good in goods]

    applications = Application.query.filter(and_(Application.good_id.in_(
        goods), Application.result == "同意")).order_by(Application.timestamp.desc()).all()

    data = [
        {
            "id": application.id,
            "result": application.result,
            "backup": application.backup,
            "timestamp": application.timestamp,
            "good_status": application.good_status,
            "driver_name": application.driver.username,
            "driver_phone": application.driver.phone_number,
            "good_name": application.good.good_name,
            "transport_origin": application.good.transport_origin,
            "transport_des": application.good.transport_des,
            "transport_money": application.good.transport_money,
        }
        for application in applications
    ]

    res["data"] = data
    return jsonify(res)


# 司机获取自己所有的申请记录
@good.route("/dapps/")
@login_required
def get_all_driver_applications():
    res = {
        "state": "success", "msg": "get applicatons successfully", "data": []
    }
    # 申请状态: all(所有货物), "同意", "拒绝", "等待审核"
    app_type = request.args.get("app_type")
    if session.get("role", None) == None or session.get("role") != "driver":
        res["state"] = "error"
        res["msg"] = "fuck you!"
        return jsonify(res)

    if app_type == None:
        app_type = "all"

    if app_type not in ["all", "同意", "拒绝", "等待审核"]:
        res["state"] = "error"
        res["msg"] = "fuck you!"
        return jsonify(res)

    driver_id = session.get("id")
    applications = []
    if app_type == "all":
        applications = Application.query.filter_by(
            driver_id=driver_id).order_by(Application.timestamp.desc()).all()
    else:
        applications = Application.query.filter(and_(
            Application.driver_id == driver_id, Application.result == app_type)).order_by(Application.timestamp.desc()).all()

    applications = [
        {
            "id": application.id,
            "result": application.result,
            "backup": application.backup,
            "timestamp": application.timestamp,
            "good_status": application.good_status,
            "driver_name": application.driver.username,
            "driver_phone": application.driver.phone_number,
            "good_name": application.good.good_name,
            "transport_origin": application.good.transport_origin,
            "transport_des": application.good.transport_des,
            "transport_money": application.good.transport_money,
            "consigner_name": application.good.consigner.username,
            "consigner_id": application.good.consigner.id,
            "consigner_phone_number": application.good.consigner.phone_number,
            "next_status": next_status(application.good_status)

        }
        for application in applications
    ]

    res["data"] = applications
    return jsonify(res)


# 司机修改货物运输的状态
@good.route("/appstatus/", methods=["POST"])
@login_required
def driver_change_transport_status():
    res = {
        "state": "success", "msg": "change applicaton-state successfully", "data": []
    }
    request_data = request.get_json()
    application_id = request_data.get("id")
    status = request_data.get("status")

    application = Application.query.get(application_id)
    application.good_status = status

    db.session.add(application)
    db.session.commit()

    return jsonify(res)

# 获取所有货物种类
@good.route("/goodtypes/")
@login_required
def get_all_goodtypes():
    res = {
        "state": "success", "msg": "get goodtypes successfully", "data": []
    }
    goodtypes = GoodType.query.order_by(GoodType.type_name.desc()).all()

    goodtypes = [
        {
            "id": goodtype.id,
            "type_name": goodtype.type_name
        }
        for goodtype in goodtypes
    ]
    res["data"] = goodtypes
    return jsonify(res)


# 货主发布货物
@good.route("/sendgood/", methods=["POST"])
@login_required
def consigner_send_good():
    res = {
        "state": "success", "msg": "change applicaton-state successfully", "data": []
    }

    request_data = request.get_json()
    good_name = request_data.get("good_name")
    good_type = request_data.get("good_type")
    transport_origin = request_data.get("transport_origin")
    transport_des = request_data.get("transport_des")
    transport_money = request_data.get("transport_money")
    transport_time = request_data.get("transport_time")
    backup = request_data.get("backup")

    try:
        good = Good(
            good_name=good_name,
            goodtype_id=good_type,
            transport_origin=transport_origin,
            transport_des=transport_des,
            transport_money=transport_money,
            transport_time=transport_time,
            backup=backup
        )
        good.consigner_id = session.get("id")

        db.session.add(good)
        db.session.commit()

    except Exception as e:
        res["msg"] = str(e)
    
    return jsonify(res)
    
