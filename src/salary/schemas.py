from datetime import date

from pydantic import BaseModel


class SalaryCreate(BaseModel):
    id: int
    salary: float
    date: date
