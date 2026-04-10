import uvicorn 
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.session import engine
from app.routers.api import api_router
from app.core.config import settings

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(api_router)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=settings.SERVICE_PORT)