from fastapi import HTTPException
from http import HTTPStatus
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User
from app.services.base_servide import BaseService
from app.repositories.unit_or_work_repository import UnitOfWorkRepositiory


class UserService(BaseService):

    def __init__(self,repo : UnitOfWorkRepositiory):
        super().__init__(repo)

    def create(self, data : UserCreate):

        user_model = User(**data.model_dump())
        user_exists = self._repository.user_repo.get_user_by_email(user_model.email)
        
        if user_exists != None:
            raise HTTPException(status_code=HTTPStatus.CONFLICT , detail= {"mensagem":"usuários existente"})
    
        return self._repository.user_repo.create(user_model)
    
     
       

    def get(self, user_id :int):
        if self._repository.user_repo.get(user_id) == None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail= {"mensagem":"usuário não encontrado"})  

        return self._repository.user_repo.get(user_id)
    
    def get_task(self, user_id :int):
        self.get(user_id)
        return self._repository.task_repository.assegneted_user(user_id)