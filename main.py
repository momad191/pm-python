from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# from .graphs.supervisor_graph import graph
from app.graphs.supervisor_graph import graph 

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
)





app = FastAPI()


app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=False,

    allow_methods=["*"],

    allow_headers=["*"],
)


 
class Question(BaseModel):
    question: str
    openai_api_key: str
    thread_id: str | None = None


@app.get("/")
def home():

    return {

        "status": "success",

    }


# @app.post("/chat")
# def chat(
#     request: Question,
# ):

#     state = {

#         "messages": [],

#         "question": request.question,

#         "answer": "",

#         "selected_agent": "",

#         "project_action": "",

#         "tool_name": "",

#         "tool_result": "",

#         "context": {},

#     }

#     result = graph.invoke(

#         state,

#         config={

#             "configurable": {

#                 "thread_id": "6a39a2a0d118161c6526a72b",

#             }

#         },

#     )

#     return result



 
@app.post("/chat")
def chat(request: Question):

    config = {
        "configurable": {
            "thread_id": request.thread_id or "default-thread",
        }
    }

    state = {
        "question": request.question,
    }

    if request.openai_api_key:
        state["openai_api_key"] = request.openai_api_key

    result = graph.invoke(
        state,
        config=config,
    )

    return result