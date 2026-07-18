from langgraph.graph import StateGraph
from langgraph.graph import START, END

from .state import AgentState

from .nodes import (
    analyze_node,
    greeting_node,
    prompt_node,
    ai_node,
    format_node,
    route_question,
    tool_router_node,
    calculator_node,
    route_tool
)

from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
 
builder = StateGraph(AgentState)


builder.add_node("analyze", analyze_node)
# builder.add_node("greeting", greeting_node)
builder.add_node("tool_router", tool_router_node)
builder.add_node("calculator", calculator_node)
builder.add_node("prompt", prompt_node)
builder.add_node("ai", ai_node)
builder.add_node("format", format_node)



# builder.add_edge(START, "ai")
# builder.add_edge("ai", END)


builder.add_edge(START, "analyze")
# builder.add_conditional_edges(
#     "analyze",
#     route_question,
#     {
#         "greeting": "greeting",
#         "prompt": "prompt",
#     }
# )
builder.add_edge("analyze","tool_router")
builder.add_conditional_edges(

    "tool_router",

    route_tool,

    {

        "calculator": "calculator",

        "ai": "prompt",

    }

)

builder.add_edge("calculator","format")

# builder.add_edge("greeting", "format")
builder.add_edge("prompt", "ai")
builder.add_edge("ai", "format")
builder.add_edge("format", END)



# graph = builder.compile()

graph = builder.compile(
    checkpointer=memory
)