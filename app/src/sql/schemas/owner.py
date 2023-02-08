from pydantic import BaseModel

class OwnerBase(BaseModel):
    id: int
    contactLastName: str
    contactFirstName: str
    phone: str

class Owner(OwnerBase):
    email: str
    identification_number: str
    id_approved: bool
    class Config:
        orm_mode = True

class OwnerCreate(OwnerBase):
    email: str
    identification_number: str

class OwnerUpdate(OwnerBase):
    email: str

class OwnerDelete(OwnerBase):
    email: str


