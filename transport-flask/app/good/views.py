from app.good import good
from flask import request, jsonify
from app.models import Good
from app.extensions import db
from app.utils import login_required
import pysnooper


# 获取所有可利用的，即处于"等待司机承运"状态的货物
@good.route("/goods")
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
            "username": good.consigner.username
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