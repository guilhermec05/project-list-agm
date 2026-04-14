from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.project import Project
from datetime import datetime

class ProjectRepository:
    def __init__(self, session :Session):
        self.__session = session

    def create(self,project : Project):
        self.__session.add(project)
        self.__session.commit()
        self.__session.refresh(project)
        return project

    def get_all(self,offset:int =0, limit:int=100):
        return self.__session.execute(select(Project)
                                   .where(Project.deleted_at == None)
                                   .offset(offset).limit(limit)).scalars().all()
    
    def get(self, id :int):
        return self.__session.execute(select(Project)
                                   .where(Project.id == id  )
                                   .where( Project.deleted_at == None)
                                ).scalar()
    

    def update(self, id:int ,project:Project ):       
        project_model = self.get(id)
        
        if project_model == None:
            return None   

        project_model.description = project.description
        project_model.name =  project.name
        self.__session.add(project_model)
        self.__session.commit()
        self.__session.refresh(project_model)
        
        return project_model    


    def soft_delete(self, id:int):
        project_model = self.get(id)

        if project_model == None :
            return False
        
        project_model.deleted_at = datetime.now()
        self.__session.add(project_model)
        self.__session.commit()
        self.__session.refresh(project_model)
        
        return True