from http import HTTPStatus
from fastapi import HTTPException
from .base_servide import BaseService
from app.repositories.unit_or_work_repository import UnitOfWorkRepositiory
from app.schemas.task import TaskCreate
from app.models.task import Task

class TaskService(BaseService):

    def __init__(self,repo : UnitOfWorkRepositiory):
        super().__init__(repo)


    def __get_project(self, id :int):
        project = self._repository.project_repo.get(id)
        if project == None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail={"mensagem":"tareja não existe"})

    
    def create(self,project_id :int,task :TaskCreate):
        self.__get_project(project_id)
        if task.assignee_id != None :
            user = self._repository.user_repo.get(task.assignee_id)

            if user == None :
                  raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail={"mensagem":"usuário não existe"})



        task_model = Task(**task.model_dump())
        task_model.project_id = project_id

        return self._repository.task_repository.create(task_model)
    
    def list_by_project(self, project_id :int):
        self.__get_project(project_id)
        return self._repository.task_repository.get_by_project(project_id)