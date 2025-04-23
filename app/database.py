from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from .Models import Base
from sqlalchemy.orm import sessionmaker 
sqlite_file_name = "postgresql://postgres:123asd$@localhost/postgres"
# connect_args = {"check_same_thread": False}
engine = sa.create_engine(sqlite_file_name,echo=True)

Base.metadata.create_all(engine)

session_local = sessionmaker(autoflush=False,autocommit=False,bind=engine)
session = session_local()

