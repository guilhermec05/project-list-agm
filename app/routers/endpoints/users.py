
from http import HTTPStatus
from fastapi import APIRouter,Depends,Response
from app.services.user_service import UserService
from app.schemas.user import UserRead,UserCreate
from app.schemas.task import TaskRead
from app.routers.deps import get_user_service
from .base_endpoint import result
#from app.core.security import get_current_user,permission_router

router = APIRouter(prefix="/Users", tags=["Usuários"])

@router.post("/",status_code=HTTPStatus.CREATED,
             response_model=UserRead,
              name="Cria usuário"
            )
def create_user(data: UserCreate , 
                session : UserService = Depends(get_user_service)
                ):
    return result(session.create(data))

@router.get("/{user_id}",status_code=HTTPStatus.OK,
            response_model=UserRead,
            name="Busca usuário por id"
)           
def get_list(user_id : int, 
             session : UserService =  Depends(get_user_service)
            ):
    return result(session.get(user_id))


@router.get("/{user_id}/tasks",status_code=HTTPStatus.OK,
            response_model=list[TaskRead],
            name="Busca lista de tarefas atribuidas por usuário"
)        
def get_tasks(user_id : int, 
             session : UserService =  Depends(get_user_service)
            ):
    return  result(session.get_task(user_id))



