from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

SQLALCHEMY_DATABASE_URL = 'postgresql://admin:123@localhost:5432/TestTaskDB'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()







