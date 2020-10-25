from flask import Blueprint

from datetime import datetime


generic_urls_blueprint = Blueprint("generic_urls", __name__)


@generic_urls_blueprint.route("/")
def index():
    return {"message":"success"}

@generic_urls_blueprint.route("/today")
def get_today():
    return {"today": datetime.now().strftime("%A, %d. %B %Y %I:%M%p")}