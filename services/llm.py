from langchain_openai import ChatOpenAI

from ..config import settings


llm = ChatOpenAI(
    model=settings.OPENAI_MODEL,
    temperature=settings.OPENAI_TEMPERATURE,
    api_key=settings.OPENAI_API_KEY,
)