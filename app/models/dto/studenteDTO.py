from datetime import date
from typing import Optional
from sqlmodel import SQLModel


class ShowStudente(SQLModel):
    id:int
    name:str
    surname:str

class StudenteUpdate(SQLModel):
    name:Optional[str]
    surname:Optional[str]
    date_of_birth:Optional[date]
    classe_id:Optional[int]