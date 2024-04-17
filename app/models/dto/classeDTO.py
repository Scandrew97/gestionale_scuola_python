from ..dto.studenteDTO import ShowStudente
from ..models import Anno, Studente

from typing import List, Optional
from sqlmodel import SQLModel

class ClasseUpdate(SQLModel):
    anno:Optional[Anno]= None
    sezione:Optional[str]= None
    # studenti:Optional[List[Studente]]= None

class ShowClasse(SQLModel):
    id:int
    anno:int
    sezione:str
    # studenti: List[ShowStudente]