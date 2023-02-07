from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True, index=True)
    contactLastName = Column(String(50), unique=True, index=True, nullable=False)
    contactFirstName = Column(String(50), index=True, unique=True, nullable=False)
    identification_number = Column(String(50), index=True, unique=True, nullable=False)
    email = Column(String(50), index=True, unique=True, nullable=False)
    is_approved = Column(Boolean, default=False)
    
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True, nullable=False)
    content = Column(String(100), index=True, unique=True, nullable=False)
    is_approved = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("owners.id"), default=1)
    owner = relationship("Owner", back_populates="posts")




