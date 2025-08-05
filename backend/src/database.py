from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABSE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABSE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()
