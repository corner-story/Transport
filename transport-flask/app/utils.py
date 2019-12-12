from flask import session, make_response
from functools import wraps

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