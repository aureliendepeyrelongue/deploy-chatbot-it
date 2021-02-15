
from .models import User, Conversation, Solution
from flask_bcrypt import Bcrypt
import json

bcrypt = Bcrypt()
from flask import session
from .models import User
from .models import Conversation
from datetime import datetime
from app import bcrypt
from sqlalchemy import desc

class Service:
    #inititate encryption utilitity 
    def __init__(self, db):
        self.db = db

    # Function to load chat training data
    #function to register the user information
    def register(self, first_name, last_name, email, password, user_service):
        self.validate_email(email)
        user = User(first_name,last_name, email, password,user_service)
        self.db.session.add(user)
        self.db.session.commit()
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email).first()
        if user is not None:
            raise ValueError('Please use a different email address.')

    #Login function
    def login(self, email, password):
        is_valid=False
        # get user in db from password + email
        user = User.query.filter_by(email=email).first()
        if user:
            is_valid=user.is_correct_password(password)
        if is_valid:
            return user
        else:
            return None
    
    def get_history_keys_and_last_conversation(self, user_id):
        conversations = self.db.session.query(Conversation.id).filter_by(user_id=user_id).order_by(Conversation.id.desc()).all()
        last_conversation = Conversation.query.filter_by(user_id=user_id).order_by(Conversation.id.desc()).first()
        if conversations and last_conversation:
            return {"conversations_ids": (list(map(lambda c: c[0], conversations))),
            "last_conversation": {"id": last_conversation.id, "content": json.loads(last_conversation.content), "created_on": last_conversation.createdon, "was_helpful": last_conversation.was_helpful}}
        else:
            return None
   

    def get_conversations_ids(self, user_id):
        conversations = self.db.session.query(Conversation.id).filter_by(user_id=user_id).order_by(Conversation.id.desc()).all()
        if conversations:
            return {"conversations_ids": (list(map(lambda c: c[0], conversations)))}
        else:
            return None
   

    def get_history_conversation(self, user_id,conversation_id):
        conversation = Conversation.query.filter_by(user_id=user_id, id=conversation_id).first()
        if conversation:
            return {"id": conversation.id, "content": json.loads(conversation.content), "created_on": conversation.createdon, "was_helpful": conversation.was_helpful}
        else:
            return None

    #Save conversation
    def save_conversation(self,content, was_helpful):
        user_id=session.get("user_id")
        #if "user_id" not in session:
        #   user_id = 1

        conv=Conversation(user_id,content,was_helpful)
        self.db.session.add(conv)
        self.db.session.commit()

    def get_user_conversations(self,user_id):
        convs= Conversation.query.filter_by(user_id=user_id).all()
        return convs
        
    def add_new_solution(self,user_id, problem_text, solution_text, conversation_id):
        solution = Solution(user_id, problem_text, solution_text, conversation_id)
        self.db.session.add(solution)
        self.db.session.commit()
        return solution

    def get_solutions_for_admin_app(self):
        solutions = Solution.query.all()

        for s in solutions:
            s.user = User.query.filter_by(id=s.user_id).first()
            s.conversation = Conversation.query.filter_by(id=s.conversation_id).first()
            if s.conversation == None:
                s.conversation_content = '{"items": []}'
            else:
                 s.conversation_content = s.conversation.content

        return list(map(lambda s: {"solution_id" : s.id, "problem" : s.problem, "solution" : s.solution, "username" : s.user.first_name + " " + s.user.last_name, "conversation" :  json.loads( s.conversation_content), "approved" : s.approved}, solutions))

    def update_solution_for_admin_app(self, solution_id, approved):
        print(solution_id)
        
        Solution.query.filter_by(id=solution_id).update(dict(approved=approved))
        self.db.session.commit()
        self.db.session.rollback()
       
     



#exports 