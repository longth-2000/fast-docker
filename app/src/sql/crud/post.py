from sqlalchemy.orm import Session

from app.src.sql import models
from app.src.sql.schemas import post

def get_post(db: Session, post_id: int): 
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def create_post(db:Session, post: post.PostCreate):
    db_post = models.Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
    
