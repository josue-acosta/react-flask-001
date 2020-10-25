from flask import Blueprint
from api import app

from datetime import datetime


generic_urls_blueprint = Blueprint("generic_urls", __name__)


@generic_urls_blueprint.route("/")
def index():
    return app.send_static_file("index.html")



@generic_urls_blueprint.route("/today")
def get_today():
    return {"today": datetime.now().strftime("%A, %d. %B %Y %I:%M%p")}