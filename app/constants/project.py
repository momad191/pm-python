from enum import StrEnum


class ProjectAction(StrEnum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    LIST = "list"
    DETAILS = "details"
    SEARCH = "search"
    ARCHIVE = "archive"
    RESTORE = "restore"
    STATISTICS = "statistics"
    GENERAL = "general"