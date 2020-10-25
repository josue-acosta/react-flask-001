from flask import Flask


# app config
app = Flask(__name__)
app.config.from_object("api.configuration.DevelopmentConfig")

# register blueprints
from api.generic_urls.views import generic_urls_blueprint
app.register_blueprint(generic_urls_blueprint, url_prefix='/v1/api')