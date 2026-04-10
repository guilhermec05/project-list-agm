from sqlmodel import Session,select
from app.models.task import Task

class TaskRepository:
    
    def __init__(self, session :Session):
        self.__session = session

    def create(self,task:Task) -> Task:
        self.__session.add(task)
        self.__session.commit()
        self.__session.refresh(task)
        return task
    
    def get_by_project(self,id:int):
        return self.__session.exec(select(Task).where(Task.project_id == id)).all()