from enum import StrEnum


class AgentName(StrEnum):
    MANAGER = "manager"
    PROJECT = "project"
    TASK = "task"
    ISSUE = "issue"
    REPORT = "report"
    GENERAL = "general"