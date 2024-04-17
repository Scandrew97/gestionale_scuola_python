from fastapi import APIRouter, status
from ..models.models import User
from ..models.dto.userDTO import ShowUser
from ..repository import user


router=APIRouter(prefix='/user', tags=['USER'])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: User):
    return user.create(request)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=ShowUser)
def update(id, request: User):
    return user.update(request)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id):
    return user.delete(id)