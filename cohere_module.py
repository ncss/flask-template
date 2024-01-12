from langchain_community.chat_models import ChatCohere
from langchain_core.messages import HumanMessage
from langchain_community.embeddings import CohereEmbeddings
from dotenv import load_dotenv

load_dotenv()

llm = ChatCohere(model="command", temperature=0.3)
embeddings = CohereEmbeddings(mode="")

prompt = HumanMessage(
    content=""
)
message = "Make a rap"

print(llm.invoke(message))