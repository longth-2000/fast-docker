from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "mysql://root:secret@localhost:3308/db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String(50))
    model = Column(String(50))
    owner_id = Column(Integer, ForeignKey("owners.id"))

    # define relationship with owner
    owner = relationship("Owner", back_populates="cars")

# define owner model
class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    cars = relationship("Car", back_populates="owner")

# create tables in database
Base.metadata.create_all(bind=engine)

# define input model for creating a car
class CarCreate(BaseModel):
    make: str
    model: str

# define input model for creating an owner
class OwnerCreate(BaseModel):
    name: str

# define output model for a car
class CarSchema(BaseModel):
    id: int
    make: str
    model: str
    owner_id: int

# define output model for an owner
class OwnerSchema(BaseModel):
    id: int
    name: str
    cars: list[CarSchema]

app = FastAPI()

# dependency for getting db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create car for owner with specified ID
@app.post("/owners/{owner_id}/cars/", response_model=CarSchema)
def create_car_for_owner(
    owner_id: int, car: CarCreate, db: Session = Depends(get_db)
):
    db_owner = db.query(Owner).filter(Owner.id == owner_id).first()
    if not db_owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    db_car = Car(**car.dict(), owner=db_owner)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# create owner with cars
@app.post("/owners/", response_model=OwnerSchema)
def create_owner(owner: OwnerCreate, cars: list[CarCreate], db: Session = Depends(get_db)):
    db_owner = Owner(**owner.dict())
    db_cars = [Car(**car.dict(), owner=db_owner) for car in cars]
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    # db_owner.cars.extend(db_cars)
    # db.commit()
    # db.refresh(db_owner)
    return db_owner
