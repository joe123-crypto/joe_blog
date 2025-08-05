from sqlalchemy import Column, Integer, String, Text,DateTime
from src.database import Base
from datetime import datetime

class BlogPost(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(200),nullable=False)
    content = Column(Text,nullable=False)
    author = Column(String(100),nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow)
