from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .src.sql import crud, models, schemas
from .src.sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/posts/")
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)










