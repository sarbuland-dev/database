from models import user
from db import sessionlocal


def create_user(name:str,email:str):
    with sessionlocal as session:
        user=user(name=name,email=email)
        session.add(user)
        session.commit()