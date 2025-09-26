from db import engine
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column
from sqlalchemy import String

class base(DeclarativeBase):
    pass

class user(base):
    __tablename__="users"
    
    id:Mapped[int]=mapped_column(nullable=False,primary_key=True)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    email:Mapped[str]=mapped_column(String(50),nullable=False,unique=True)
    
   

def create_table():
    base.metadata.create_all(engine)
