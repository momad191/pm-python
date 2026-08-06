from typing import Annotated
from typing_extensions import TypedDict
from typing import TypedDict

from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):

    # PART 4 Create Memory
    messages: Annotated[list[BaseMessage], add_messages]
    question: str
    openai_api_key: str
    intent: str
    prompt: str
    answer: str 
    tool_name: str
    tool_result: str 