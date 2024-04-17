from ..database.db import session
from sqlmodel import select
from ..models.models import Studente
from ..models.dto.studenteDTO import StudenteUpdate
from fastapi import HTTPException, status
from . import classe as cl

def get_all():
    studenti= session.exec(select(Studente)).all()
    if not studenti:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Non ci sono studenti')
    return studenti

def get_by_id(id):
    studente= session.get(Studente, id)
    if not studente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Studente con ID: {id} non trovato')
    return studente

def get_by_nome(name):
    studenti= session.exec(select(Studente).where(Studente.name==name)).all()
    if not studenti:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Studente {name} non trovato')
    return studenti
    
def get_by_cognome(surname):
    studenti= session.exec(select(Studente).where(Studente.surname==surname)).all()
    if not studenti:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Studente {surname} non trovato')
    return studenti
    
def get_by_classe(anno, sezione):
    classe = cl.get_by_anno_sezione(anno, sezione)
    if not classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Classe {anno} {sezione} non trovata')
    studenti= session.exec(select(Studente).where(Studente.classe_id==classe.id)).all()
    if not studenti:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Classe {anno} {sezione} vuota')
    return studenti

def create(anno, sezione, request: Studente):
    classe = cl.get_by_anno_sezione(anno, sezione)
    if not classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Classe {anno} {sezione} non trovata')
    new_studente= Studente(name=request.name, surname=request.surname, date_of_birth=request.date_of_birth, classe_id=classe.id)
    session.add(new_studente)
    session.commit()
    session.refresh(new_studente)
    return new_studente

def update(id, request: StudenteUpdate):
    studente= get_by_id(id)
    if not studente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Studente con ID: {id} non trovato')
    updated_studente= request.model_dump(exclude_unset=True)
    studente.sqlmodel_update(updated_studente)
    session.add(studente)
    session.commit()
    session.refresh(studente)
    return studente

def delete(id):
    studente= session.get(Studente, id)
    session.delete(studente)
    session.commit()    
    

    
    



    