from flask import session
from .Chatbot.prediction import Chatbot
from .models import Conversation, ChatItem, ChatSession,ChatResponse

from .Chatbot.training import Chatbot as train
import json
from app import service

bot = Chatbot("Miage")

class ChatbotManager:
    
    #Start the converstion methodd
    @staticmethod
    def start_conversation():
        intent="start_conversation"
        previous_chat_session=Chatbot_Utils.getChatSession()
        if(len(previous_chat_session.items) > 1):
            service.save_conversation(session["current_conversation"],False)
            session.pop("current_conversation")
            
        cs=ChatSession(items=[])
        msg=bot.get_response(intent)
        start_item=ChatItem("<SOC>", msg, "start_conversation","")
        cs.addItem(start_item)
        Chatbot_Utils.saveChatSession(cs)
        return  ChatResponse("<SOC>",msg)
        
    #reply message
    @staticmethod
    def reply(message):
        intent, response = bot.predict_response(message)
        if len(intent)>0:
            current_chat=Chatbot_Utils.getChatSession()
            item = ChatItem("Q", message, intent,"c")
            current_chat.addItem(item)
            item = ChatItem("A", response, intent,"c")
            current_chat.addItem(item)
            Chatbot_Utils.saveChatSession(current_chat)
        if intent.lower()=="goodbye" or intent.lower()=="thanks":
            intent="<EOC>"
        
        return ChatResponse(intent,response)

    #End the converation method
    @staticmethod
    def end_conversation(washelpful):
        chat_session=Chatbot_Utils.getChatSession()
        
        res=chat_session.to_Json()
        if(len(chat_session.items) > 1):
            service.save_conversation(chat_session.to_Json(),washelpful)
            session.pop("current_conversation")
           
        return res
            
    
    # train method if we want to train the bot again, we can use this method from admin site
    @staticmethod
    def train():
        t = train(5000)
        t.train()


    
class Chatbot_Utils:
    #get the current conversation
    @staticmethod
    def getChatSession():
        if "current_conversation" not in session:
            cs=ChatSession(items=[])
            Chatbot_Utils.saveChatSession(cs)
        
        return ChatSession.from_json(session["current_conversation"])

    #Set current conversation
    @staticmethod
    def saveChatSession(cs):
        session["current_conversation"]=cs.to_Json()


