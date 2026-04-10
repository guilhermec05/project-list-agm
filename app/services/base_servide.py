
from app.repositories.unit_or_work_repository import UnitOfWorkRepositiory

class BaseService:
    def __init__(self, repository: UnitOfWorkRepositiory ):
        self._repository = repository