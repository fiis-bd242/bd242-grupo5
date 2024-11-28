# import reflex as rx
# import sqlalchemy

# from datetime import date, datetime
# from typing import Optional
# from enum import Enum


# # Definición de ENUMs
# class EstadoContrato(str, Enum):
#     Activo = "Activo"
#     Finalizado = "Finalizado"
#     Suspendido = "Suspendido"


# class JornadaLaboral(str, Enum):
#     Completa = "Completa"
#     Parcial = "Parcial"
#     TurnoRotativo = "Turno rotativo"


# class EstadoRecobro(str, Enum):
#     Enviado = "Enviado"
#     Valorizando = "Valorizando"
#     Pendiente = "Pendiente"
#     Ejecutado = "Ejecutado"
#     Completado = "Completado"


# class EstadoProyecto(str, Enum):
#     Ejecutado = "Ejecutado"
#     Supervision = "Supervision"


# class EstadoSolicitud(str, Enum):
#     Abierto = "Abierto"
#     Cerrado = "Cerrado"


# class EstadoInquilino(str, Enum):
#     Activo = "Activo"
#     Inactivo = "Inactivo"


# class EstadoEspacioComun(str, Enum):
#     Ocupado = "Ocupado"
#     Disponible = "Disponible"
#     EnMantenimiento = "En mantenimiento"


# class EstadoFactura(str, Enum):
#     Pendiente = "Pendiente"
#     Pagado = "Pagado"


# class TipoRecordatorio(str, Enum):
#     Previo = "Previo"
#     Posterior = "Posterior"


# class EstadoMantenimiento(str, Enum):
#     Pendiente = "Pendiente"
#     Hecho = "Hecho"


# class EstadoContratoAlquiler(str, Enum):
#     Activo = "Activo"
#     Expirado = "Expirado"
#     Renovado = "Renovado"


# class EstadoIncidencia(str, Enum):
#     Pendiente = "Pendiente"
#     Programado = "Programado"


# class TipoInstalacion(str, Enum):
#     Zona = "Zona"
#     Tienda = "Tienda"
#     Modulo = "Modulo"


# class MetodoPago(str, Enum):
#     Manual = "Manual"
#     Automatico = "Automatico"


# # Tablas definidas como modelos Reflex
# class ContratoEmpleado(rx.Model, table=True):
#     id_contrato_empleado: str
#     descripcion_cargo: str
#     fecha_inicio: date
#     fecha_fin: date
#     estado_contrato: EstadoContrato
#     jornada_laboral: JornadaLaboral


# class Persona(rx.Model, table=True):
#     id_persona: str
#     nombre: str
#     nro_domicilio: int
#     ciudad: str
#     nro_documento: str
#     tipo_documento: str


# class Empleado(rx.Model, table=True):
#     id_empleado: str
#     cargo: str
#     first_last_name: str
#     second_last_name: str
#     fecha_nacimiento: date
#     id_persona: str
#     id_contrato_empleado: str


# class Recobro(rx.Model, table=True):
#     id_recobro: str
#     nombre_recobro: str
#     descripcion_recobro: str
#     razon_recobro: str
#     categoria_recobro: str
#     estado_recobro: EstadoRecobro


# class ProyectoRecobro(rx.Model, table=True):
#     id_proyecto: str
#     nombre_proyecto: str
#     costos: float
#     estado_proyecto: EstadoProyecto
#     fecha_inicio_proyecto: date
#     fecha_fin_proyecto: date
#     id_recobro: str


# class Documento(rx.Model, table=True):
#     id_documento: str
#     tipo_documento: str
#     fecha_subido: date


# class Solicitud(rx.Model, table=True):
#     id_solicitud: str
#     estado_solicitud: EstadoSolicitud
#     fecha_solicitud: date
#     fecha_resolucion: date
#     id_documento: str


# class Zona(rx.Model, table=True):
#     id_zona: str
#     piso: int
#     referencia: str
#     nombre_zona: str


# class Actividad(rx.Model, table=True):
#     cod_actividad: str
#     nombre_actividad: str
#     descripcion: str
#     fecha_inicio_actividad: date
#     fecha_fin_actividad: date
#     costo_actividad: float
#     estado_actividad: str
#     id_proyecto: str


# class PersonaEmail(rx.Model, table=True):
#     email: str
#     id_persona: str


# class PersonaTelefono(rx.Model, table=True):
#     telefono: int
#     id_persona: str


# class Prioridad(rx.Model, table=True):
#     prioridad: str
#     descrip_prioridad: str


# class Instalacion(rx.Model, table=True):
#     id_instalacion: str
#     nombre_instalacion: str
#     id_zona: str


# class EspacioComercial(rx.Model, table=True):
#     id_espacio_comercial: str
#     tipo_inmueble: str
#     estado: str
#     area: float
#     tarifa: float
#     id_zona: str


# class Inquilino(rx.Model, table=True):
#     id_inquilino: str
#     razon_social: str
#     fecha_eliminacion: Optional[date]
#     fecha_registro: date
#     estado_inquilino: EstadoInquilino
#     id_persona: str
#     id_espacio_comercial: str


# class EspacioComun(rx.Model, table=True):
#     id_espacio_comun: str
#     estado: EstadoEspacioComun
#     area: float
#     precio_por_dia: float
#     motivo_de_uso: str
#     id_zona: str


# class Factura(rx.Model, table=True):
#     id_factura: str
#     estado_factura: EstadoFactura
#     fecha_emision: date
#     monto_total: float
#     fecha_vencimiento: date
#     id_inquilino: str


# class Recordatorio(rx.Model, table=True):
#     id_recordatorio: str
#     tipo_recordatorio: TipoRecordatorio
#     fecha_envio: date
#     contenido: str
#     id_factura: str


# class Pago(rx.Model, table=True):
#     id_pago: str
#     fecha_pago: date
#     metodo_pago: MetodoPago
#     monto_pago: float
#     tipo_moneda: str
#     id_factura: str


# class Evento(rx.Model, table=True):
#     id: str
#     nombre_evento: str
#     descripcion: str
#     categoria: str
#     objetivo: str
#     fecha_inicio: date
#     fecha_fin: date
#     id_espacio_comun: str
#     id_inquilino: str


# class RegistroIncidencia(rx.Model, table=True):
#     cod_incidencia: int
#     descripcion: str
#     fecha_hora_registro: datetime
#     estado: EstadoIncidencia
#     id_instalacion: str
#     id_empleado: str


# class ProgramMantenimiento(rx.Model, table=True):
#     dod_mantenimiento: int
#     plazo: date
#     descripcion: str
#     estado: EstadoMantenimiento
#     id_instalacion: str
#     id_encargado: str
#     prioridad: str
#     cod_incidencia: Optional[int]


# class AcuerdoRecobro(rx.Model, table=True):
#     id_acuerdo: str
#     fecha_acuerdo: date
#     descripcion_acuerdo: str
#     precio_acuerdo: int
#     id_proyecto: str
#     id_factura: str


# class ContratoAlquiler(rx.Model, table=True):
#     id_contrato: str
#     fecha_inicio: date
#     monto: float
#     condicion: str
#     fecha_vencimiento: date
#     estado: EstadoContratoAlquiler
#     porcentaje: float
#     id_documento: str
#     id_factura: str
#     id_espacio_comercial: str


# class RegistroMantenimiento(rx.Model, table=True):
#     cod_r_mantenimiento: int
#     observaciones: Optional[str]
#     fecha_realizada: date
#     hora_inicio: datetime
#     hora_fin: datetime
#     id_instalacion: str
#     dod_mantenimiento: int
#     id_empleado: str