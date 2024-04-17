from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select
from ..models.models import User
from ..models.dto.tokenDTO import Login
from ..database.db import session
from ..security.hashing import Hash as hs
from ..security.jwt import create_access_token

router=APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends()):
    user = session.exec(select(User).filter(User.email==request.username)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credential')
    if not hs.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Password')
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}