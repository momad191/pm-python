
import os
import re
 

from dotenv import load_dotenv 

from langchain_openai import ChatOpenAI
from .state import AgentState
from .tools import calculator

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
)


load_dotenv()

print(os.getenv("OPENAI_API_KEY"))

llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0,
)








def extract_expression(question: str) -> str:

    question = question.lower()

    question = re.sub(
        r"(calculate|what is|what's|compute)",
        "",
        question,
    )

    return question.strip()


# PART ONE NODE

# def ai_node(state: AgentState):
#     response = llm.invoke(state["question"])
#     return {
#         "answer": response.content
#     }



# PART2 MULTIPLE NODES

# def analyze_node(state: AgentState):

#     question = state["question"]

#     print("=" * 40)
#     print("Analyze Node")
#     print(question)

#     return {
#         "intent": "general_question"
#     }



# PART3 Conditional Routing
def analyze_node(state: AgentState):

    question = state["question"].lower().strip()

    print("=" * 40)
    print("Analyze Node")

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening",
    ]

    if question in greetings:
        intent = "greeting"
    else:
        intent = "general_question"

    print(f"Intent: {intent}")

    return {
        "intent": intent
    }



# PART3 Conditional Routing
def greeting_node(state: AgentState):

    print("=" * 40)
    print("Greeting Node")

    return {
        "answer": "Hello 👋\n\nWelcome! How can I help you today?"
    }


# PART3 Conditional Routing
def route_question(state: AgentState):

    print("=" * 40)
    print("Routing...")

    if state["intent"] == "greeting":
        return "greeting"

    return "prompt"




# PART2 MULTIPLE NODES

# def prompt_node(state: AgentState):

#     prompt = f"""
# You are an expert AI assistant.

# Question:

# {state["question"]}

# Answer clearly and professionally.
# """

#     print("=" * 40)
#     print("Prompt Node")

#     return {
#         "prompt": prompt
#     }


# Part 4 to create Memory
def prompt_node(state: AgentState):

    history_count = len(state["messages"])

    prompt = f"""
You are an AI assistant.

Conversation contains {history_count} previous messages.

Current Question:

{state["question"]}

Answer naturally while keeping the conversation context.
"""

    return {
        "prompt": prompt
    }


# PART 1 create Nodes

# def ai_node(state: AgentState):
#     print("=" * 40)
#     print("AI Node")
#     response = llm.invoke(state["prompt"])
#     return {
#         "answer": response.content
#     }


# PART 4 Create Memory
# def ai_node(state: AgentState):

#     print("=" * 40)
#     print("AI Node")

#     messages = state["messages"]

#     messages.append(
#         HumanMessage(content=state["prompt"])
#     )

#     response = llm.invoke(messages)

#     return {
#         "answer": response.content,
#         "messages": [
#             AIMessage(content=response.content)
#         ]
#     }

# Part 5  to Create Tools
def ai_node(state: AgentState):

    print("=" * 40)
    print("AI Node")

    if state["tool_result"]:

        prompt = f"""
The calculator returned:

{state["tool_result"]}

Explain the result to the user.
"""

        response = llm.invoke(prompt)

    else:

        messages = state["messages"]

        messages.append(

            HumanMessage(

                content=state["prompt"]

            )

        )

        response = llm.invoke(messages)

    return {

        "answer": response.content,

        "messages": [

            AIMessage(

                content=response.content

            )

        ]

    }



def format_node(state: AgentState):

    formatted = f"""
AI Response

--------------------------------

{state["answer"]}
"""

    print("=" * 40)
    print("Format Node")

    return {
        "answer": formatted
    }



# Part 5  to Create Tools

def tool_router_node(state: AgentState):

    question = state["question"].lower()

    print("=" * 40)
    print("Tool Router")

    math_words = [

        "+",
        "-",
        "*",
        "/",
        "calculate",
        "multiply",
        "divide",
        "add",
        "subtract",
    ]

    if any(word in question for word in math_words):

        return {

            "tool_name": "calculator"

        }

    return {

        "tool_name": "none"

    }


# Part 5  to Create Tools
def route_tool(state: AgentState):

    if state["tool_name"] == "calculator":

        return "calculator"

    return "ai"


# Part 5  to Create Tools
def calculator_node(state: AgentState):

    print("=" * 40)
    print("Calculator Tool")

    question = state["question"].lower()

    

    # expression = (

    #     question

    #     .replace("calculate", "")

    #     .replace("what is", "")

    #     .strip()

    # )


    expression = extract_expression(state["question"])

    result = calculator.invoke(

        {

            "expression": expression

        }

    )

    return {

        "tool_result": result,

        "answer": f"The answer is {result}"

    }


 