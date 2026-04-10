from fastapi import HTTPException,Response
from http import HTTPStatus
from app.services.base_servide import BaseService
from app.repositories.unit_or_work_repository import UnitOfWorkRepositiory
from app.schemas.project import ProjectCreate,ProjectUpdate
from app.models.project import Project

class PojectService(BaseService):
    def __init__(self, repository: UnitOfWorkRepositiory ):
        super().__init__(repository)
    
    def create(self,project:ProjectCreate):
        project_model = Project(**project.model_dump())
        project_obj =  self._repository.user_repo.get(project_model.ower_id)

        if project_obj == None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail={"mensagem":"projeto não existe"})

        return self._repository.project_repo.create(project_model)
    
    def get_all(self, offset:int = 0, limit:int = 100):
        return self._repository.project_repo.get_all(offset,limit)
    
    def get(self, id:int):
        project = self._repository.project_repo.get(id)
        if project == None :
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail={"mensagem":"projeto não existe"})
        
        return project
    
    def update(self, id:int,project:ProjectUpdate):
        project_model = Project(**project.model_dump())
        project_return = self._repository.project_repo.update(id,project_model)
        
        if project_return == None :
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail={"mensagem":"projeto não existe"})
        
        return project_return
    
    def delete(self, id:int):
        is_deleted = self._repository.project_repo.soft_delete(id)
        
        if not is_deleted:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND,detail={"mensagem":"projeto não existe"})
        
        return {"mensagem":"deletado com sucesso"}