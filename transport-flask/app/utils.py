from flask import session, make_response
from functools import wraps
import pysnooper

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kw):
        if(session.get("islogin", None) is None):
            res = {
                "state": "error"
                ,"msg": "你tm先登录!"
                ,"data":{}
            }
            return make_response(res, 403)
        return func(*args, **kw)
    return wrapper  

# 根据货物当前状态获取下一个状态
@pysnooper.snoop()
def next_status(curr):
    status = ["等待司机承运", "选定司机", "正在运输", "已到达目的地", "运输完成", "确定"]
    if curr == None or curr not in status:
        return "无法操作"
    return status[status.index(curr)+1]





if __name__ == "__main__":
    import json

    class Test(object):
        def __init__(self, name, age, friends):
            self.name = name
            self.age = age
            self.friends = friends

    test = Test("wsl", "18", ["f1", "f2"])

    res = json.dumps(test, default=lambda obj: obj.__dict__)

    print(type(res))
    print(res)
