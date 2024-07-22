from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


metadata = Base.metadata


class Example(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, autoincrement=True)
    test_val = Column(String(100))
