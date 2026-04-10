
from http import HTTPStatus
from fastapi import APIRouter,Depends,Response
from app.services.user_service import UserService
from app.schemas.user import UserRead,UserCreate
from app.routers.deps import get_user_service
from .base_endpoint import result
#from app.core.security import get_current_user,permission_router

router = APIRouter(prefix="/Users", tags=["Usuários"])

@router.post("/",status_code=HTTPStatus.CREATED,
             response_model=UserRead
            )
def create_user(data: UserCreate , 
                session : UserService = Depends(get_user_service)
                ):
    return result(session.create(data))

@router.get("/{user_id}",status_code=HTTPStatus.OK,
            response_model=UserRead
)           
def get_list(user_id : int, 
             session : UserService =  Depends(get_user_service)
            ):
    return result(session.get(user_id))


@router.get("/{user_id}/tasks",status_code=HTTPStatus.OK,
            response_model=UserRead
)        
def get_tasks(user_id : int, 
             session : UserService =  Depends(get_user_service)
            ):
    return Response(status_code=HTTPStatus.OK,content={"mensagem":"ainda não foi criada"})



