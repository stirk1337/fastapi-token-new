from datetime import date

from base import Base
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


class Salary(Base):
    __tablename__ = "salary"

    id: Mapped[int] = mapped_column(
            Integer, primary_key=True
        )
    salary: Mapped[float]
    date: Mapped[date]
    user: Mapped["User"] = relationship(back_populates="salary")
