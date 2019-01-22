from flask import Flask



app = Flask(__name__, instance_relative_config=True)
from api.views import views
app.register_blueprint(views.bp)