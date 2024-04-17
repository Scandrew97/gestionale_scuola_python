from ..database.db import session
from sqlmodel import select
from ..models.models import Classe
from ..models.dto.classeDTO import ClasseUpdate
from fastapi import HTTPException, status

def get_all():
    classi= session.exec(select(Classe)).all()
    if not classi:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='Non ci sono classi')
    return classi

def get_by_id(id):
    classe= session.exec(select(Classe).where(Classe.id==id)).first()
    if not classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Classe con ID: {id} non trovata')
    return classe

def get_by_anno(anno):
    classi= session.exec(select(Classe).where(Classe.anno==anno)).all()
    if not classi:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Classi di {anno}° anno non trovate')
    return classi

def get_by_sezione(sezione):
    classi= session.exec(select(Classe).where(Classe.sezione==sezione)).all()
    if not classi:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Classi con sezione: {sezione} non trovate')
    return classi

def get_by_anno_sezione(anno, sezione):
    classe= session.exec(select(Classe).where((Classe.anno == anno) and (Classe.sezione == sezione))).first()
    if not classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Classe {anno,sezione} non trovata')
    return classe

def create(user_id, request:Classe):
    nuova_classe= Classe(anno=request.anno, sezione=request.sezione, user_id=user_id)
    session.add(nuova_classe)
    session.commit()
    session.refresh(nuova_classe)
    return nuova_classe

def update(id, request:ClasseUpdate):
    classe= session.get(Classe, id)
    if not classe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Classe con ID: {id} non trovata')
    updated_classe= request.model_dump(exclude_unset=True)
    classe.sqlmodel_update(updated_classe)
    session.add(classe)
    session.commit()
    session.refresh(classe)
    return classe

def delete(id):
    classe= session.get(Classe, id)
    session.delete(classe)
    session.commit()



