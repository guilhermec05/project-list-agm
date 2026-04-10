from datetime import datetime
from sqlmodel import SQLModel,  Field,Column,TIMESTAMP,text
from typing import Optional

class User(SQLModel,table= True):
    id: Optional[int] = Field(default=None,primary_key= True)
    name: str
    email:str = Field(unique=True)
    created_at: Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ))