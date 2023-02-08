from pydantic import BaseModel

class PostBase(BaseModel):
    id: int
    title: str
    content: str

class Post(PostBase):
    id_approved: bool
    owner_id: int
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    title: str
    content: str

class PostUpdate(PostBase):
    title: str
    content: str

class PostDelete(PostBase):
    pass



