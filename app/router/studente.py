from typing import List
from fastapi import APIRouter, status, Depends
from ..security.oauth2 import get_current_user
from ..repository import studente as st
from ..models.models import Studente, User
from ..models.dto.studenteDTO import ShowStudente, StudenteUpdate

router= APIRouter(prefix='/studente', tags=['STUDENTE'])

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowStudente])
def all(get_current_user:User=Depends(get_current_user)):
    return st.get_all()

@router.get('/id/{id}', status_code=status.HTTP_200_OK, response_model=ShowStudente)
def by_id(id,get_current_user:User=Depends(get_current_user)):
    return st.get_by_id(id)

@router.get('/nome/{nome}', status_code=status.HTTP_200_OK, response_model=List[ShowStudente])
def by_nome(nome, get_current_user:User=Depends(get_current_user)):
    return st.get_by_nome(nome)

@router.get('/cognome/{cognome}', status_code=status.HTTP_200_OK, response_model=List[ShowStudente])
def by_nome(cognome, get_current_user:User=Depends(get_current_user)):
    return st.get_by_cognome(cognome)

@router.get('/classe/{anno}/{sezione}', status_code=status.HTTP_200_OK, response_model=List[ShowStudente])
def by_classe(anno, sezione, get_current_user:User=Depends(get_current_user)):
    return st.get_by_classe(anno,sezione)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowStudente)
def create(anno, sezione, request: Studente, get_current_user:User=Depends(get_current_user)):
    return st.create(anno, sezione, request)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ShowStudente)
def update(id, request: StudenteUpdate, get_current_user:User=Depends(get_current_user)):
    return st.update(id, request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, get_current_user:User=Depends(get_current_user)):
    return st.delete(id)
