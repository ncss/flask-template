from langchain_community.chat_models import ChatCohere
from langchain_core.messages import HumanMessage
from langchain_community.embeddings import CohereEmbeddings
from dotenv import load_dotenv, dotenv_values

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

load_dotenv()

initial_prompt = open("./static/prompt.txt", "r").read()

class ChatBot:
    def __init__(self, *args, **kwargs):

        self.llm = ChatCohere(*args, **kwargs)
        self.history = [
            {"user_name": "User", "text": initial_prompt},
            {"user_name": "System", "text": "Yes."}
        ]

    def chat_invoke(self, message):

        self.history.append({"user_name": "User", "text": message})

        response = self.llm.invoke(
            input=message,
            chat_history=self.history
        )

        self.history.append({"user_name": "System", "text": response.content})

        return response
        # return self.llm.invoke(message).content