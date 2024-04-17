from fastapi import APIRouter, status, Depends
from ..security.oauth2 import get_current_user
from ..repository import classe as cl
from ..models.models import Classe , User
from ..models.dto.classeDTO import ClasseUpdate, ShowClasse
from typing import List

router=APIRouter(prefix='/classe', tags=['CLASSE'])

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowClasse])
def all(get_current_user:User=Depends(get_current_user)):
    return cl.get_all()

@router.get('/id/{id}', status_code=status.HTTP_200_OK, response_model=ShowClasse)
def by_id(id, get_current_user:User=Depends(get_current_user)):
    return cl.get_by_id(id)

@router.get('/anno/{anno}', status_code=status.HTTP_200_OK, response_model=List[ShowClasse])
def by_anno(anno, get_current_user:User=Depends(get_current_user)):
    return cl.get_by_anno(anno)

@router.get('/sezione/{sezione}', status_code=status.HTTP_200_OK, response_model=List[ShowClasse])
def by_sezione(sezione, get_current_user:User=Depends(get_current_user)):
    return cl.get_by_sezione(sezione)

@router.get('/anno_sezione/{anno}/{sezione}', status_code=status.HTTP_200_OK, response_model=ShowClasse)
def by_anno_sezione(anno, sezione, get_current_user:User=Depends(get_current_user)):
    return cl.get_by_anno_sezione(anno, sezione)

# passare user_id dal local storage
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowClasse)
def create(user_id, request:Classe, get_current_user:User=Depends(get_current_user)):
    return cl.create(user_id, request)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ShowClasse)
def update(id, request:ClasseUpdate, get_current_user:User=Depends(get_current_user)):
    return cl.update(id, request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, get_current_user:User=Depends(get_current_user)):
    return cl.delete(id)