from fastapi import APIRouter
from app.routers.endpoints import   users,project,task

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(project.router)
api_router.include_router(task.router)

