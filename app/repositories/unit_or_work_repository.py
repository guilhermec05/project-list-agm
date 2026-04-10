from sqlmodel import Session
from app.repositories.project_repository import ProjectRepository
from app.repositories.user_repository import UserRepository
from app.repositories.task_repository import TaskRepository

class UnitOfWorkRepositiory:
    
    def __init__(self,session : Session ):
        self.user_repo = UserRepository(session)
        self.project_repo = ProjectRepository(session)
        self.task_repository = TaskRepository(session)