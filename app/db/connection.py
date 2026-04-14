from app.core.config import settings
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase



engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()