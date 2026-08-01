from typing import Optional

from pydantic import BaseModel, Field

from ..constants.project import ProjectAction
from .search_context import SearchContext


class ProjectDecision(BaseModel):

    action: ProjectAction

    # Structured search intent
    search: Optional[SearchContext] = None

    # CRUD fields
    project_id: Optional[str] = Field(
        default=None,
        description="Project ID such as PRO-001",
    )

    name: Optional[str] = None

    description: Optional[str] = None

    manager_id: Optional[str] = None

    department: Optional[str] = None

    status: Optional[str] = None

    month: Optional[str] = None

    year: Optional[str] = None

    start_date: Optional[str] = None

    end_date: Optional[str] = None

    completion_percentage: Optional[int] = None

    is_deleted: Optional[bool] = None

    confidence: float = 1.0

    def normalize(self) -> "ProjectDecision":
        """
        Normalizes values into the application's canonical format.

        IMPORTANT

        This function NEVER invents values.
        It never creates dates.
        It never generates ranges.
        It never guesses years.

        It only converts user-provided values into their
        canonical representation.
        """

        month_map = {
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6,
            "july": 7,
            "august": 8,
            "september": 9,
            "october": 10,
            "november": 11,
            "december": 12,
            "يناير": 1,
            "فبراير": 2,
            "مارس": 3,
            "أبريل": 4,
            "ابريل": 4,
            "مايو": 5,
            "يونيو": 6,
            "يوليو": 7,
            "أغسطس": 8,
            "اغسطس": 8,
            "سبتمبر": 9,
            "أكتوبر": 10,
            "اكتوبر": 10,
            "نوفمبر": 11,
            "ديسمبر": 12,
        }

        status_map = {
            "نشط": "ACTIVE",
            "active": "ACTIVE",
            "ACTIVE": "ACTIVE",

            "قيد التنفيذ": "IN_PROGRESS",
            "in progress": "IN_PROGRESS",
            "IN_PROGRESS": "IN_PROGRESS",

            "مكتمل": "COMPLETED",
            "completed": "COMPLETED",
            "COMPLETED": "COMPLETED",

            "مؤجل": "ON_HOLD",
            "on hold": "ON_HOLD",
            "ON_HOLD": "ON_HOLD",

            "ملغي": "CANCELLED",
            "cancelled": "CANCELLED",
            "canceled": "CANCELLED",
            "CANCELLED": "CANCELLED",
        }

        department_map = {
            "الموارد البشرية": "HR",
            "تقنية المعلومات": "IT",
            "تكنولوجيا المعلومات": "IT",
            "المبيعات": "SALES",
            "التسويق": "MARKETING",
            "العلاقات العامة": "PR",
            "المالية": "FINANCE",
        }

        # -----------------------------
        # Root Status
        # -----------------------------
        if self.status:

            key = self.status.strip().lower()

            self.status = status_map.get(
                key,
                self.status.upper(),
            )

        # -----------------------------
        # Root Department
        # -----------------------------
        if self.department:

            key = self.department.strip().lower()

            self.department = department_map.get(
                key,
                self.department,
            )

        # -----------------------------
        # Structured Search
        # -----------------------------
        if self.search:

            if self.search.text:
                self.search.text = self.search.text.strip()

            if self.search.status:

                key = self.search.status.strip().lower()

                self.search.status = status_map.get(
                    key,
                    self.search.status.upper(),
                )

            if self.search.department:

                key = self.search.department.strip().lower()

                self.search.department = department_map.get(
                    key,
                    self.search.department,
                )

            if self.search.date:

                if self.search.date.field:
                    self.search.date.field = (
                        self.search.date.field.strip()
                    )

                if isinstance(self.search.date.month, str):

                    value = (
                        self.search.date.month
                        .strip()
                        .lower()
                    )

                    self.search.date.month = month_map.get(
                        value,
                        self.search.date.month,
                    )

        return self