from flask import Flask, render_template, request
from app.chatbot_service import ChatbotManager
from app import app

# Mainly for Chatbot AJAX call logic

@app.route("/chatbot/get-response")
def get_bot_response():
    userText = str(request.args.get('userTextMessage'))
    return ChatbotManager.reply(userText).to_json()

@app.route("/chatbot/start_chat")
def start_chat():
    return ChatbotManager.start_conversation().to_json()

@app.route("/chatbot/end_chat")
def end_chat():
    resp = request.args.get('was_helpful')
    return ChatbotManager.end_conversation(resp=="yes")

