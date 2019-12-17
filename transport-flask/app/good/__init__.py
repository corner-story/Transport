from flask import Blueprint

good = Blueprint("good", __name__)


from app.good import views