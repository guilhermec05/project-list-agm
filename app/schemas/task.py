from enum import Enum
from pydantic import BaseModel
from typing import Optional

from datetime import datetime

class StatusTask(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class PriorityTask(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskCreate(BaseModel):
    title:str
    description:str
    due_date:datetime
    status:StatusTask
    assignee_id:int  = None
    priority:PriorityTask





class TaskRead(BaseModel):
    id:int
    title:str
    description:str
    project_id:int
    due_date:datetime
    status:StatusTask
    assignee_id:int |None = 0
    priority:PriorityTask




    
class TaskUpdate(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    due_date:Optional[datetime] = None
    status:Optional[StatusTask] = None
    assignee_id:Optional[int]  = None
    priority:Optional[PriorityTask] = None