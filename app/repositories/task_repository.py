from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import PriorityTask, StatusTask

class TaskRepository:
    
    def __init__(self, session :Session):
        self.__session = session

    def create(self,task:Task) -> Task:
        self.__session.add(task)
        self.__session.commit()
        self.__session.refresh(task)
        return task
    
    def get_by_project(self,id:int,priority :PriorityTask,status: StatusTask):
        return self.__session.execute(select(Task)
                                      .where(Task.project_id == id 
                                             and Task.status == status
                                             and Task.priority ==  priority
                                             )
                                      ).scalars().all()
    
    def get(self, id:int):
        return self.__session.get(Task,id)
    
    def update(self, task_update : Task):
        model = self.get(task_update.id)

        if model == None:
            return None
        
        return self.create(task_update)

    def delete(self,task:Task):
        self.__session.delete(task)
        self.__session.commit()
        return True
    
    def assegneted_user(self , user_id :int):
        return self.__session.execute(select(Task).where(Task.assignee_id == user_id)).scalars().all()