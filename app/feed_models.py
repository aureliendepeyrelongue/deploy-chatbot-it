from app import service
from .models import Conversation, User
from datetime import datetime

conv_content = '['

for i in range(30):
        conv_content+= '{ "items": [ { "context": "c", "date": "11/02/2021, 15:43:38", "intent": "greeting", "text": "Hello", "type": "Q" }, { "context": "c", "date": "11/02/2021, 15:43:38", "intent": "greeting", "text": "Hi there, how can I help?", "type": "A" }, { "context": "c", "date": "11/02/2021, 15:43:38", "intent": "greeting", "text": "How are you", "type": "Q" }, { "context": "c", "date": "11/02/2021, 15:43:38", "intent": "greeting", "text": "Good to see you again, how I can help you", "type": "A" }, { "context": "c", "date": "11/02/2021, 15:43:38", "intent": "goodbye", "text": "Bye", "type": "Q" }, { "context": "c", "date": "11/02/2021, 15:43:38", "intent": "goodbye", "text": "Have a nice day", "type": "A" } ] }'

def feed_db():
        service.register("Alice", "Mely", "alice@chatbot.fr", "test", "MIAGE")
        service.register("Bob", "Dylan", "bob@chatbot.fr", "test", "MIAGE")

        for a in range(30):
                service.save_conversation(content=conv_content, was_helpful=False)
        for a in range(30):
                service.save_conversation(content=conv_content, was_helpful=True)
        
        for a in range(20):
                service.save_conversation(content=conv_content, was_helpful=True)
