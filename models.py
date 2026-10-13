from datetime import date,datetime

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    String,
    Text,
    func,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index = True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(),)

    applications: Mapped[list["Application"]] = relationship(back_populates="user")

class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key= True)
    name: Mapped[str] = mapped_column(String(200), index = True)
    website: Mapped[str | None] = mapped_column(String(500), nullable=True)


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), index=True)
    job_title: Mapped[str] = mapped_column(String(200))
    status: Mapped[str] = mapped_column(String(30), default="applied")
    applied_date: Mapped[date] = mapped_column(Date,default=date.today)

    notes: Mapped[str | None] = mapped_column(Text,nullable=True)

    user: Mapped["User"] = relationship(back_populates="applications")

    company: Mapped["Company"] = relationship(
        back_populates= "applications"
    )