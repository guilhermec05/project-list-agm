from sqlmodel import Session
from fastapi import Depends
from app.db.session import get_session
from app.repositories.unit_or_work_repository import UnitOfWorkRepositiory
from app.services.user_service import UserService
from app.services.project_service import PojectService
from app.services.task_service import TaskService

def get_user_service(session: Session = Depends(get_session) ) -> UserService:
    repo = UnitOfWorkRepositiory(session)
    return UserService(repo)

def get_project_service(session: Session = Depends(get_session)) ->PojectService:
    repo = UnitOfWorkRepositiory(session)
    return PojectService(repo)

def get_task_service(session: Session = Depends(get_session)) -> TaskService:
    repo = UnitOfWorkRepositiory(session)
    return TaskService(repo)
    