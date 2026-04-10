from datetime import datetime
from sqlmodel import SQLModel,  Field,Column,TIMESTAMP,text
from typing import Optional

class Project(SQLModel,table= True):
    id: Optional[int] = Field(default=None,primary_key= True)
    name: str
    description:str
    ower_id :int =  Field(default=None, foreign_key="user.id",ondelete='CASCADE')
    created_at: Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ))
    deleted_at:Optional[datetime]