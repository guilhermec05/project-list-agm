from datetime import datetime
from sqlalchemy import func
from sqlmodel import SQLModel,  Field,Column,TIMESTAMP,text,CheckConstraint
from typing import Optional

class Task(SQLModel,table= True):
    id: Optional[int] = Field(default=None,primary_key= True)
    title: str
    description:str
    status: Optional[str] = Field(default='todo',sa_column_args=(CheckConstraint("status in  ('todo','in_progress','done')")))
    priority: Optional[str] = Field(default='low',sa_column_args=(CheckConstraint("priority in  ('low','medium','high')")))
    project_id :int = Field(default=None, foreign_key="project.id",ondelete='CASCADE')
    assignee_id :Optional[int] =  Field(default=None, foreign_key="user.id",nullable=True)
    due_date: datetime
    created_at: Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ))
    update_at : Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        onupdate=func.now(),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ))
    deleted_at:Optional[datetime]