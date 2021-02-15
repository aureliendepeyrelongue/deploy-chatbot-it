
from app import db
from app import bcrypt
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import json
from typing import List
from app import app

#User Class
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(200))
    service = db.Column(db.String(50))
    is_admin=db.Column(db.Boolean)

    #One to Many relation
    conversation=relationship("Conversation")

    def __init__(self,first_name,last_name, email, plaintext_password, user_service):
        self.first_name=first_name
        self.last_name=last_name
        self.email = email
        self.password=bcrypt.generate_password_hash(plaintext_password)
        self.service=user_service
        self.is_admin=False
    
    def is_correct_password(self, plaintext_password: str):
        return bcrypt.check_password_hash(self.password, plaintext_password)

    def set_password(self, plaintext_password):
        self.password = bcrypt.generate_password_hash(plaintext_password)

#Class conversation
class Conversation(db.Model):
    __tablename__ = 'conversations'
    #id=db.Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    content=db.Column(db.String(500))
    createdon=db.Column(db.DateTime)
    was_helpful=db.Column(db.Boolean)
    
    #default constructor
    def __init__(self,user_id,content,was_helpful=False):
        self.user_id=user_id
        self.content=content
        self.createdon=datetime.now()
        self.was_helpful=was_helpful

# class for saving the conversation structure
class ChatItem:
    def __init__(self,type,text,intent,context,date=""):
        self.type=type
        self.text=text
        self.intent=intent
        self.context=context
        self.date=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    
    @classmethod
    def from_json(cls, data):
        return cls(**data)

#Class to hold the current session chat items
class ChatSession():
    def __init__(self, items: List[ChatItem]):
        self.items = items

    def addItem(self, item: ChatItem):
        self.items.append(item)
    
    @classmethod
    def from_json(cls, data):
        data=json.loads(data)
        items = list(map(ChatItem.from_json, data["items"]))
        return cls(items)
    
    def to_Json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

#ChatResponse class
class ChatResponse():
    def __init__(self,intent,msg):
        self.intent=intent
        self.msg=msg
    
    def to_json(self):
        return self.__dict__

#Class conversation
class Solution(db.Model):
    __tablename__ = 'solutions'
    #id=db.Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    problem = db.Column(db.String(500))
    solution = db.Column(db.String(500))
    conversation_id= db.Column(db.Integer, db.ForeignKey('conversations.id'))
    createdon = db.Column(db.DateTime)
    approved=db.Column(db.Boolean)
    
    #default constructor
    def __init__(self,user_id,problem,solution,conversation_id=None):
        self.user_id=user_id
        self.problem=problem
        self.solution=solution
        self.conversation_id = conversation_id
        self.createdon = datetime.now()
        self.approved = False
    
#create the tables 
with app.app_context():
    db.create_all()

