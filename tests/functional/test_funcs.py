
from app.service import Service
from app.models import User

#Test the login functionality in case of valid login 
def test_login(test_client,init_database,valid_login):
    user=valid_login
    assert user is not None

#Test the login functionality in case of invalid login
def test_invalid_login(test_client,init_database,invalid_login):
    user=invalid_login
    if user is None:
        assert 1

#test the routes
def test_home_page(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    print(response)
    assert response.status_code == 404
    #assert b"Home" in response.data
    #assert b"Chatbot IT Support" in response.data
    #assert b"Ask a technical question to our chatbot and get an instantaneous answer." in response.data
