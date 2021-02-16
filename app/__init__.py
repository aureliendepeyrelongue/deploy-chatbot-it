from flask import Flask
from datetime import timedelta
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db=SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    #initiate the application 
    flask_app = Flask(__name__)
    #set the configuration
    flask_app.config.from_object('configs.DevConfigs')
    #initiate the db connection
    db.init_app(flask_app)
    #create the Bcrypt insyance 
    bcrypt.init_app(flask_app)

    return flask_app

#create the app
app =create_app()

# import the service module
from .service import Service
service = Service(db)


#import the controllers
from app import chatbot_controller
from app import common_controller
from app import user_controller
from app import admin_controller

#set the session timeout in app
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

