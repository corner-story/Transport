from flask import session, redirect, url_for
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kw):
        if(session.get("islogin", None) is None):
            return redirect(url_for("login"))
        return func(*args, **kw)
    return wrapper        