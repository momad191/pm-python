from typing import Literal

from pydantic import BaseModel
 

class ManagerDecision(BaseModel):

    agent: Literal[
        "project",
        "task",
        "issue",
        "report",
        "general",
    ]