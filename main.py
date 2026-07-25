from fastapi import FastAPI
from pydantic import BaseModel

# from .graphs.supervisor_graph import graph
from app.graphs.supervisor_graph import graph


app = FastAPI()


class Question(BaseModel):

    question: str


@app.get("/")
def home():

    return {

        "status": "success",

    }


@app.post("/chat")
def chat(
    request: Question,
):

    state = {

        "messages": [],

        "question": request.question,

        "answer": "",

        "selected_agent": "",

        "project_action": "",

        "tool_name": "",

        "tool_result": "",

        "context": {},

    }

    result = graph.invoke(

        state,

        config={

            "configurable": {

                "thread_id": "6a39a2a0d118161c6526a72b",

            }

        },

    )

    return result