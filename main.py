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
    # thread_id: str
    question: str


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
            "thread_id": "6a39a2a0d118161c6526a72b",
            # "thread_id": request.thread_id,
        }
    }


    snapshot = graph.get_state(config)

    print(snapshot.values)

    state = {
        "question": request.question,
    }

    result = graph.invoke(
        state, 
        config=config,
    )

    return result