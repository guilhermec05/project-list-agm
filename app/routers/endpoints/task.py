from fastapi import APIRouter,Depends
from http import HTTPStatus
from app.schemas.task import TaskCreate,TaskRead
from app.routers.deps import get_task_service
from app.services.task_service import TaskService
from app.routers.endpoints.base_endpoint import result 

router = APIRouter(tags=["Tarefas"])

@router.post("/project/{project_id}/tasks",status_code=HTTPStatus.CREATED,
             response_model=TaskRead
            )
def create(
    project_id : int,
    data: TaskCreate , 
                session : TaskService = Depends(get_task_service)
                ):
    return result(session.create(project_id,data))