from enum import StrEnum

class IssueAction(StrEnum):
    CREATE = "create"
    UPDATE = "update"
    CLOSE = "close"
    REOPEN = "reopen"
    LIST = "list"
    SEARCH = "search"