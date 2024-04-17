from fastapi import FastAPI
from sqlmodel import SQLModel
from .models import models
from .database.db import engine
from .router import auth, classe, user, studente

app=FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(classe.router)
app.include_router(user.router)
app.include_router(studente.router)