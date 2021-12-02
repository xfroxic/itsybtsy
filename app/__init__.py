from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_manager

# __name__ is a predefined variable in Python, which is set to the name of the module in which it's used
# passing __name__ almost always configures Flask in the correct way
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view='login'

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'users.login'

# importing routes at the bottom of the script helps avoid circular imports
from app import routes, models