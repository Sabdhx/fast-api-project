from sqlalchemy import String,Integer,Column,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime 
 
Base = declarative_base()

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True,autoincrement=True,nullable=False)
  title = Column(String,nullable=False)
  content = Column(String,nullable=False)
  published = Column(bool,nullable=False)
  created_at = Column(DateTime, default = datetime.utcnow, nullable=False)