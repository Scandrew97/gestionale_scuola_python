from ..database.db import session
from sqlmodel import select
from ..models.models import User
from fastapi import HTTPException, status, encoders
from ..security.hashing import Hash as hs

def create(request: User):
    new_user=User(
        name=request.name, 
        surname=request.surname, 
        email=request.email,
        password=hs.bcrypt(request.password))
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

def update(id, request: User):
    user= session.get(User, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User con ID: {id} non trovato')
    updated_user= user.model_dump(exclude_unset=True)
    user.sqlmodel_update(updated_user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete(id):
    user= session.get(User, id)
    session.delete(user)
    session.commit()