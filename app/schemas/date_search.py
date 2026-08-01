from enum import Enum
from pydantic import BaseModel


class DateField(str, Enum):
    START_DATE = "startDate"
    END_DATE = "endDate"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"


class DateSearch(BaseModel):

    field: DateField | None = None

    exact: str | None = None

    from_date: str | None = None

    to_date: str | None = None

    month: int | None = None

    year: int | None = None