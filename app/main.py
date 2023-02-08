from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.src.sql import models
from app.src.sql.database import SessionLocal, engine
from app.src.sql.schemas import post as post_schema 
from app.src.sql.crud import post as post_crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    return post_crud.get_post(db=db, post_id=post_id)


@app.post("/posts/")
def create_post(post: post_schema.PostCreate, db: Session = Depends(get_db)):
    return post_crud.create_post(db=db, post=post)











