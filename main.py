# from dotenv import load_dotenv
# load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from agent.graph import graph


app = FastAPI()

class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "status": "success"
    }


@app.post("/chat")
def chat(request: Question):

    result = graph.invoke(
        {
            "messages": [],
            "question": request.question,
            "intent": "",
            "prompt": "",
            "answer": ""
        },
        config={

        "configurable": {
            "thread_id": "demo-user"
          }
        }
    )

    return result



