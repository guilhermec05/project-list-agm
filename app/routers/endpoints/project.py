
from http import HTTPStatus
from fastapi import APIRouter,Depends,Query
from app.services.project_service import PojectService
from app.schemas.project import ProjectCreate,ProjectRead,ProjectUpdate
from app.routers.deps import get_project_service
from .base_endpoint import result

router = APIRouter(prefix="/Project", tags=["Projetos"])

@router.post("/",status_code=HTTPStatus.CREATED,
             response_model=ProjectRead,
            name="Cria projeto"
            )
def create_project(data: ProjectCreate , 
                session : PojectService = Depends(get_project_service)
                ):
    return result(session.create(data))

@router.get("/",status_code=HTTPStatus.OK,
            response_model=list[ProjectRead],
             name="Lista projetos(com paginação)"
)           
def get_project(offset: int = 0, 
               limit: int = Query(default=100, le=100) ,
               session : PojectService =  Depends(get_project_service)
            ):
    return result(session.get_all(offset, limit))


@router.get("/{task_id}",status_code=HTTPStatus.OK,
            response_model=ProjectRead,
              name="busca projeto por id"
)           
def get(task_id:int,  session : PojectService =  Depends(get_project_service)):
    return result(session.get(task_id))


@router.put("/{task_id}",status_code=HTTPStatus.OK,
            response_model=ProjectRead,
              name="atualiza projeto"
)           
def update(task_id:int,  
           data: ProjectUpdate,
           session : PojectService =  Depends(get_project_service)):
    return result(session.update(task_id,data))


@router.delete("/{task_id}",status_code=HTTPStatus.OK,
 name="remove projeto(soft delete)"
)           
def update(task_id:int,  
           session : PojectService =  Depends(get_project_service)):
    return result(session.delete(task_id))
