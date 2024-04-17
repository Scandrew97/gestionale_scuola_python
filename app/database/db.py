from sqlmodel import Session, create_engine
from ..models import models

DATABESE_URL = "mysql://root:root@localhost:3306/school_manager"

engine = create_engine(DATABESE_URL, echo=True)

session = Session(bind=engine)
