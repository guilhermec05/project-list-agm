from fastapi import APIRouter,Depends
from http import HTTPStatus
from app.schemas.task import TaskCreate,TaskRead
from app.routers.deps import get_task_service
from app.services.task_service import TaskService
from app.schemas.task import StatusTask, PriorityTask,TaskRead, TaskUpdate
from app.routers.endpoints.base_endpoint import result 

router = APIRouter(tags=["Tarefas"])

@router.post("/project/{project_id}/tasks",status_code=HTTPStatus.CREATED,
             response_model=TaskRead,
             name="cria tarefa dentro de um projeto"
           
            )
def create(
    project_id : int,
    data: TaskCreate , 
                session : TaskService = Depends(get_task_service)
                ):
    return result(session.create(project_id,data))

@router.get("/project/{project_id}/tasks",status_code=HTTPStatus.OK,
             response_model=list[TaskRead],
             name="lista as tarefas dentro de um projeto"
            )
def get_by_project(
    project_id : int,
    status: StatusTask = StatusTask.todo ,
    priority : PriorityTask = PriorityTask.low,
                session : TaskService = Depends(get_task_service)
                ):
    return result(session.list_by_project(project_id,priority, status))


@router.get("/task/{task_id}",status_code=HTTPStatus.OK,
             response_model=TaskRead,
             name="busca tarefas por id"
            )
def get_by_project(
    task_id : int,
    session : TaskService = Depends(get_task_service)
    ):
    return result(session.get(task_id))


@router.patch("/task/{task_id}",status_code=HTTPStatus.OK,
             response_model=TaskRead,
             name="atualiza tarefas parcialmente"
            )
def get_by_project(
    task_id : int,
    data : TaskUpdate,
    session : TaskService = Depends(get_task_service)
    ):
    return result(session.update(task_id,data))


@router.delete("/task/{task_id}",status_code=HTTPStatus.OK,
             name="deleta tarefas"
            )
def delete(
    task_id : int,
    session : TaskService = Depends(get_task_service)
    ):
    return result(session.delete(task_id))