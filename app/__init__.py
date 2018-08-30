from flask import Flask, Blueprint
from app.api import api
import os


basedir = os.path.dirname(os.path.abspath(__file__))
db_file = 'sqlite:///' + os.path.join(basedir, './db/grouphasrole.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import tables  
from app.api.group_has_role import ns as grouphasrole_api

blueprint = Blueprint('api', __name__, url_prefix='/grouphasrole')
api.init_app(blueprint)

api.add_namespace(grouphasrole_api)

app.register_blueprint(blueprint)