
import pytest
from flask import Flask
from app.models import User
from app import db, bcrypt
from app.service import Service

def create_test_app():
    #initiate the application 
    flask_app = Flask(__name__)
    #set the configuration
    flask_app.config.from_object('configs.TestConfigs')
    #initiate the db connection
    db.init_app(flask_app)
    #create the Bcrypt insyance 
    bcrypt.init_app(flask_app)

    return flask_app

@pytest.fixture(scope='module')
def new_user():
    user = User("first_name","last_name","test@parisnanterre.fr","plaintext_pass","service1")
    
    return user


@pytest.fixture(scope='module')
def test_client():
    #initiate the application 
    flask_app = create_test_app()
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def test_client_request():
    #initiate the application 
    flask_app = create_test_app()
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.test_request_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User("f_test_1","l_test_1","test1@gmail.com","password_test_1","s_test_1")
    user2 = User("f_test_2","l_test_22","test2@gmail.com","password_test_2","s_test_2")
    
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

@pytest.fixture(scope='module')
def valid_login():
    service=Service(db)
    return service.login("test1@gmail.com","password_test_1")

@pytest.fixture(scope='module')
def invalid_login():
    service=Service(db)
    return service.login("test1@gmail.com","password_test_2")

 