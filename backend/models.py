from sqlalchemy import Column, Integer, String

from database import Base


class Todo(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    description = Column(String)