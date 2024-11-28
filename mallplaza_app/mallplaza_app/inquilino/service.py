import reflex as rx
from .repository import select_all, select_inquilino_by_name, create_inquilino, delete_inquilino
from .model import Inquilino

def select_all_inquilino_service():
    inquilino = select_all()
    print(inquilino)
    return inquilino

def select_inquilino_by_name_service(name: str):
    if(len(name) != 0):
        return select_inquilino_by_name(name)
    else:
        return select_all()
    
def create_inquilino_service(id_inquilino: str, razon_social: str, fecha_registro: str, estado_inquilino: str, id_persona: str, id_espacio_comercial: str):
    inquilino = select_inquilino_by_name(razon_social)
    if(len(inquilino)==0):
        inquilino_save = Inquilino(id_inquilino=id_inquilino, razon_social=razon_social, fecha_registro=fecha_registro, estado_inquilino=estado_inquilino, id_persona=id_persona,id_espacio_comercial=id_espacio_comercial)
        return create_inquilino(inquilino_save)
    else:
        print("El usuario ya existe")
        raise BaseException('El usuario ya existe')
    
def delete_inquilino_service(razon_social: str):
    return delete_inquilino(razon_social=razon_social)