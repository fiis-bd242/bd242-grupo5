import reflex as rx

from .model import Inquilino
from ..database import engine
from sqlmodel import Session, select


def select_all():
    with Session(engine) as session:
        query = select(Inquilino)
        return session.exec(query).all() # SELECT * FROM inquilino
    
def select_inquilino_by_name(name: str):
    with Session(engine) as session:
        query = select(Inquilino).where(Inquilino.razon_social == name)
        return session.exec(query).all() # SELECT * FROM inquilino WHERE razon_social == 'Nombre'
    
def create_inquilino(inquilino:Inquilino):
    with Session(engine) as session:
        session.add(inquilino)
        session.commit()
        query = select(Inquilino)
        return session.exec(query).all()
    
def delete_inquilino(razon_social: str):
    with Session(engine) as session:
        query = select(Inquilino).where(Inquilino.razon_social == razon_social)
        inquilino_delete = session.exec(query).one()
        session.delete(inquilino_delete)
        session.commit()
        query = select(Inquilino)
        return session.exec(query).all()