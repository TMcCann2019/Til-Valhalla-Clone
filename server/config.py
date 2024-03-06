import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(
    __name__,
    static_url_path = "",
    static_folder="../client/build",
    template_folder="../client/build"
)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(engine_options={"echo": True})
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)
db.init_app(app)

Api.error_router = lambda self, handler, e: handler(e)
api = Api(app)