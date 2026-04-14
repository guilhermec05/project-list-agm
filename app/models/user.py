from app.db.connection import Base
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.sql import func 


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    created_at= Column(DateTime, nullable=False, default=func.now())
