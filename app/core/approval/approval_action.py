from enum import Enum


class ApprovalAction(str, Enum):

    DELETE_PROJECT = "delete_project"

    DELETE_USER = "delete_user"

    DELETE_EMPLOYEE = "delete_employee"

    DELETE_COMPANY = "delete_company"

    ARCHIVE_PROJECT = "archive_project"

    SEND_EMAIL = "send_email"