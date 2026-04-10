from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name:str
    description:str
    ower_id:int


class ProjectRead(BaseModel):
    id:int
    name:str
    description:str
    ower_id:int

class ProjectUpdate(ProjectCreate):
    pass