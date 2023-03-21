from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship, joinedload
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import sqlalchemy
from pydantic import BaseModel

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "mysql://root:secret@localhost:3308/db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    posts = relationship("Post", back_populates="author")
    


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
   

Base.metadata.create_all(bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

class UserSchema(BaseModel):
    name: str
    age: Optional[int] = 18

users = [
    {"name": "Alice"},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

@app.get("/users", response_model=list[UserSchema])
async def get_users():
    return users






