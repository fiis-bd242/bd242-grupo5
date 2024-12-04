'''
from ..model.espacio_comercial_model import Espacio_comercial
from .connect_db import connect
from sqlmodel import Session, select, desc

def select_all():
    engine = connect()
    with Session(engine) as session:
        query = select(Espacio_comercial)
        return session.exec(query).all()
    
def select_ec_by_tipo_inmueble(tipo_inmueble: str):
    engine = connect()
    with Session(engine) as session:
        query = select(Espacio_comercial).where(Espacio_comercial.tipo_inmueble == tipo_inmueble)
        return session.exec(query).all()   

def order_ec_by_tarifa ():
      engine = connect()
      with Session(engine) as session:
          query = select(Espacio_comercial).order_by(desc(Espacio_comercial.tarifa))
          return session.exec(query).all()
      
def order_ec_by_area():
    engine = connect()
    with Session(engine) as session:
        query = select(Espacio_comercial).order_by(desc(Espacio_comercial.area))
        return session.exec(query).all()
'''
