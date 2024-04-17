from typing import List, Optional
from sqlmodel import SQLModel

from .classeDTO import ShowClasse

class ShowUser(SQLModel):
    name: str
    surname: str
    email: str
    password: str
    classi:List[ShowClasse]

class UserUpdate(SQLModel):
    name:Optional[str]=None
    surname:Optional[str]=None
    password:Optional[str]=None