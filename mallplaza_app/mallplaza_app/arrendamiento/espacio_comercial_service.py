'''
from ..repository.espacio_comercial_repository import select_all, select_ec_by_tipo_inmueble, order_ec_by_tarifa, order_ec_by_area, select_ec_figma


def select_all_espacio_comercial_service():
    espacios_comerciales = select_all()
    print(espacios_comerciales)
    return espacios_comerciales

def select_ec_by_tipo_inmueble_service(tipo_inmueble: str):
    if(len(tipo_inmueble) != 0):
        return select_ec_by_tipo_inmueble(tipo_inmueble)
    else:
        return select_all_espacio_comercial_service()
    
def order_ec_by_tarifa_service():
    espacios_comerciales = order_ec_by_tarifa()
    print(espacios_comerciales)
    return espacios_comerciales #borrar

def order_ec_by_area_service():
    espacios_comerciales = order_ec_by_area()
    print(espacios_comerciales)
    return espacios_comerciales

#prueba

def select_ec_figma_service():
    contratos_alquiler = select_ec_figma()
    print(contratos_alquiler)
    return contratos_alquiler
'''
