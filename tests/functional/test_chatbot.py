from app.chatbot_service import ChatbotManager
from app.models import ChatResponse

#test the start chat function
def test_start_chat(test_client_request, init_database):
    resp=ChatbotManager.start_conversation()
    assert resp.intent=="<SOC>"

#test the start chat function
def test_chat(test_client_request, init_database):
    client_msg="Hello"
    resp=ChatbotManager.reply(client_msg)
    assert resp.intent.lower()=="greeting"

    client_msg="I have a problem"
    resp=ChatbotManager.reply(client_msg)
    assert resp.intent.lower()=="options"

    client_msg="Bye"
    resp=ChatbotManager.reply(client_msg)
    assert resp.intent=="<EOC>"

    