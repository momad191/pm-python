from enum import StrEnum

class TaskAction(StrEnum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    ASSIGN = "assign"
    COMPLETE = "complete"
    LIST = "list"
    SEARCH = "search"