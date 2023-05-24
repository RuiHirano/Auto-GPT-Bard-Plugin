from .settings import settings
from Bard import Chatbot

class BardChatbot:
    def __init__(self):
        self.chatbot = Chatbot(settings.BARD_SESSION_TOKEN)
    
    def chat_with_bard(self, question: str):
        answer = self.chatbot.ask(question)
        return answer["content"]
