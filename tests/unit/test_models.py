from app.models import User


#test creating new user instance with fixture new_user defined in conftest.py
def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password are defined correctly
    """
    assert new_user.email == 'test@parisnanterre.fr'
    assert new_user.password != 'plaintext_password'
