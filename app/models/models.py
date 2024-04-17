from datetime import date
from enum import IntEnum
from sqlmodel import SQLModel, Field, Relationship, AutoString
from typing import Optional, List
from pydantic import EmailStr


class Anno(IntEnum):
    PRIMA = 1
    SECONDA = 2
    TERZA = 3
    QUARTA = 4
    QUINTA = 5

class Livello(IntEnum):
    PRIMA_ACQUISIZIONE = 1
    BASE = 2
    INTERMEDIO = 3
    AVANZATO = 4

class User(SQLModel, table=True):
    id: Optional[int]=Field(default=None, primary_key=True)
    name:str
    surname:str
    email: EmailStr= Field(unique=True, index=True, sa_type=AutoString)
    password:str

    classi:Optional[List["Classe"]]= Relationship(back_populates='user')

    materie:Optional[List["Materia"]]= Relationship(back_populates='user')

class Classe(SQLModel, table=True):
    id: Optional[int]=Field(default=None, primary_key=True)
    anno:Optional[Anno]= None
    sezione:str

    user_id:int = Field(default=None, foreign_key='user.id')
    user:Optional[User] = Relationship(back_populates='classi')

    studenti:List["Studente"]=Relationship(sa_relationship_kwargs={"cascade":"all"}, back_populates='classe')
    # studenti:List["Studente"]=Relationship(back_populates='classe')

class MateriaStudenteLink(SQLModel, table=True):
    studente_id: Optional[int]= Field(default=None, foreign_key='materia.id' ,primary_key=True)
    materia_id: Optional[int]= Field(default=None, foreign_key='studente.id' ,primary_key=True)

class Studente(SQLModel, table=True):
    id: Optional[int]=Field(default=None, primary_key=True)
    name:str
    surname:str
    date_of_birth:date

    classe_id:int = Field(default=None, foreign_key='classe.id')
    classe:Optional[Classe] = Relationship(back_populates='studenti')

    materie: List["Materia"] = Relationship(back_populates="studenti", link_model=MateriaStudenteLink)

    verifiche: List["Verifica"] = Relationship(sa_relationship_kwargs={"cascade":"all"},back_populates='studente')

class Materia(SQLModel, table=True):
    id: Optional[int]=Field(default=None, primary_key=True)
    nome:str

    user_id:int = Field(default=None, foreign_key='user.id')
    user:Optional[User] = Relationship(back_populates='materie')

    studenti: List[Studente] = Relationship(back_populates="materie", link_model=MateriaStudenteLink)

    obiettivi: List["Obiettivo"] = Relationship(back_populates="materia")

    verifiche: List["Verifica"] = Relationship(back_populates='materia')

class Obiettivo(SQLModel, table=True):
    id: Optional[int]=Field(default=None, primary_key=True)
    descrizione:str

    materia_id: int = Field(default=None, foreign_key='materia.id')
    materia:Optional["Materia"]= Relationship(back_populates='obiettivi')

    votazione: Optional["Votazione"] = Relationship(back_populates="obiettivo")

class Votazione(SQLModel, table=True):
    id: Optional[int]=Field(default=None, primary_key=True)
    livello:Optional[Livello] = None

    obiettivo_id:int = Field(default=None, foreign_key="obiettivo.id")
    obiettivo: Optional[Obiettivo] = Relationship( back_populates="votazione")

class Verifica(SQLModel, table=True):
    id: Optional[int]=Field(default=None, primary_key=True)
    data_esecuzione:date

    materia_id: int = Field(default=None, foreign_key='materia.id')
    materia:Optional[Materia]= Relationship(back_populates='verifiche')

    studente_id: int = Field(default=None, foreign_key='studente.id')
    studente:Optional[Studente]= Relationship(back_populates='verifiche')

    esito: Optional["Esito"] = Relationship(back_populates="verifica")

class Esito(SQLModel, table=True):
    id: Optional[int]=Field(default=None, primary_key=True)
    descrizione_esito:str

    verifica_id: int = Field(default=None, foreign_key='verifica.id')
    verifica:Optional[Verifica]= Relationship(back_populates="esito")
