from sqlalchemy.orm import Session

from app.src.sql import models
from app.src.sql.schemas import owner

def get_owner(db: Session, owner_id: int):
    return db.query(models.Owner).filter(models.Owner.id == owner_id).first()

def create_owner(db: Session, owner: owner.OwnerCreate):
    db_owner = models.Owner(
        id=owner.id
        contactLastName=owner.contactLastName
        contactFirstName=owner.contactFirstName
        identification_number=owner.identification_number
        email=owner.email
    )
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

