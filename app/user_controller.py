
from flask import render_template, request
from flask_cors import cross_origin
from app import app, service
from flask import session
from flask import jsonify
#from .chatbot_service import ChatbotManager

@app.route("/user/new-solution",methods=['POST'])
@cross_origin()
def post_new_solution():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            problem_text = request.json['problem_text']
            solution_text = request.json['solution_text']
            add_reference = request.json['add_reference']
            conversation_id = request.json["conversation_id"]

    if session.get("authenticated"):
        user_id = session.get("user_id")
    else:
        user_id = 1
    
    service.add_new_solution(user_id, problem_text, solution_text,conversation_id)
      
    return "success"

@app.route("/user/chatbot-page")
def get_chatbot_page():
    if "current_conversation" in session:
        session.pop("current_conversation")
        
    return render_template("pages/user/chatbot.html")

@app.route("/user/history")
def get_history_page():
    return render_template("pages/user/history.html")

@app.route("/user/history/keys")
def get_history_keys():
    if session.get("authenticated") == True:
        user_id = session.get("user_id")
    else:
        user_id = 1

    return jsonify(service.get_history_keys_and_last_conversation(user_id))

@app.route("/user/history/conversation/<id>")
def get_history_conversation(id):
    if session.get("authenticated"):
        user_id = session.get("user_id")
    else:
        user_id = 1
    return jsonify(service.get_history_conversation(user_id, conversation_id=id))

@app.route("/user/history/ids")
def get_conversations_ids():
    if session.get("authenticated"):
        user_id = session.get("user_id")
    else:
        user_id = 1
    return jsonify(service.get_conversations_ids(user_id))