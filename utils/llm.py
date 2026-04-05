from langchain_community.chat_models import ChatOllama
from config.settings import settings

llm = ChatOllama(model=settings.MODEL_NAME)


def call_llm(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.content.strip()