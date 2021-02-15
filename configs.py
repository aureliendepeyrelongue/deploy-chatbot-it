
class DevConfigs():
   #Bcrypt secret key
    SECRET_KEY = "123e4567-e89b-12d3-a456-426614174000"

    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/chatbotDB.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 15

class TestConfigs():
   #Bcrypt secret key
    SECRET_KEY = "426614174000"

    DEBUG = True
    TESTING = True
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data/chatbotDB_test.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 4
 