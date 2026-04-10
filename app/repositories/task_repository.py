from sqlmodel import Session
from app.models.task import Task

class TaskRepository:
    
    def __init__(self, session :Session):
        self.__session = session

    def create(self,task:Task) -> Task:
        self.__session.add(task)
        self.__session.commit()
        self.__session.refresh(task)
        return task
