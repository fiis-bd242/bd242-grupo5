from sqlalchemy import (
    create_engine, Column, String, Integer, Float, Date, ForeignKey, Enum, Numeric, Time, Text, CHAR
)
from sqlalchemy.dialects.postgresql import ENUM, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKeyConstraint
import uuid

Base = declarative_base()

# Definiciones de los tipos ENUM en PostgreSQL
estado_contrato = ENUM('Activo', 'Finalizado', 'Suspendido', name='estado_contrato')
jornada_laboral = ENUM('Completa', 'Parcial', 'Turno rotativo', name='jornada_laboral')
estado_recobro = ENUM('Enviado', 'Valorizando', 'Pendiente', 'Ejecutado', 'Completado', name='estado_recobro')
estado_proyecto = ENUM('Ejecutado', 'Supervision', name='estado_proyecto')
estado_solicitud = ENUM('Abierto', 'Cerrado', name='estado_solicitud')
estado_inquilino = ENUM('Activo', 'Inactivo', name='estado_inquilino')
estado_espacio_comun = ENUM('Ocupado', 'Disponible', 'En mantenimiento', name='estado_espacio_comun')
estado_factura = ENUM('Pendiente', 'Pagado', name='estado_factura')
tipo_recordatorio = ENUM('Previo', 'Posterior', name='tipo_recordatorio')
estado_mantenimiento = ENUM('Pendiente', 'Hecho', name='estado_mantenimiento')
estado_contrato_alquiler = ENUM('Activo', 'Expirado', 'Renovado', name='estado_contrato_alquiler')
estado_incidencia = ENUM('Pendiente', 'Programado', name='estado_incidencia')
tipo_instalacion = ENUM('Zona', 'Tienda', 'Modulo', name='tipo_instalacion')
metodo_pago = ENUM('Manual', 'Automatico', name='metodo_pago')

# Creación de clases para las tablas
class ContratoEmpleado(Base):
    __tablename__ = 'contrato_empleado'
    id_contrato_empleado = Column(CHAR(10), primary_key=True)
    descripcion_cargo = Column(String(50), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    estado_contrato = Column(estado_contrato, nullable=False)
    jornada_laboral = Column(jornada_laboral, nullable=False)

class Persona(Base):
    __tablename__ = 'persona'
    id_persona = Column(CHAR(10), primary_key=True)
    nombre = Column(String(15), nullable=False)
    nro_domicilio = Column(Integer, nullable=False)
    ciudad = Column(String(30), nullable=False)
    nro_documento = Column(String(11), nullable=False)
    tipo_documento = Column(String(20), nullable=False)

class Empleado(Base):
    __tablename__ = 'empleado'
    id_empleado = Column(CHAR(10), primary_key=True)
    cargo = Column(String(50), nullable=False)
    first_last_name = Column(String(20), nullable=False)
    second_last_name = Column(String(20), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    id_persona = Column(CHAR(10), ForeignKey('persona.id_persona'), nullable=False)
    id_contrato_empleado = Column(CHAR(10), ForeignKey('contrato_empleado.id_contrato_empleado'), nullable=False)

class Recobro(Base):
    __tablename__ = 'recobro'
    id_recobro = Column(CHAR(10), primary_key=True)
    nombre_recobro = Column(String(20), nullable=False)
    descripcion_recobro = Column(String(50), nullable=False)
    razon_recobro = Column(String(30), nullable=False)
    categoria_recobro = Column(String(20), nullable=False)
    estado_recobro = Column(estado_recobro, nullable=False)


class ProyectoRecobro(Base):
    __tablename__ = 'proyecto_recobro'
    id_proyecto = Column(CHAR(10), primary_key=True)
    nombre_proyecto = Column(String(30), nullable=False)
    costos = Column(Float, nullable=False)
    estado_proyecto = Column(estado_proyecto, nullable=False)
    fecha_inicio_proyecto = Column(Date, nullable=False)
    fecha_fin_proyecto = Column(Date, nullable=False)
    id_recobro = Column(CHAR(10), ForeignKey('recobro.id_recobro'), nullable=False)

class Documento(Base):
    __tablename__ = 'documento'
    id_documento = Column(CHAR(10), primary_key=True)
    tipo_documento = Column(String(50), nullable=False)
    fecha_subido = Column(Date, nullable=False)

class Solicitud(Base):
    __tablename__ = 'solicitud'
    id_solicitud = Column(CHAR(10), primary_key=True)
    estado_solicitud = Column(estado_solicitud, nullable=False)
    fecha_solicitud = Column(Date, nullable=False)
    fecha_resolucion = Column(Date, nullable=False)
    id_documento = Column(CHAR(10), ForeignKey('documento.id_documento'), nullable=False)

class Zona(Base):
    __tablename__ = 'zona'
    id_zona = Column(CHAR(5), primary_key=True)
    piso = Column(Integer, nullable=False)
    referencia = Column(String(256), nullable=False)
    nombre_zona = Column(String(25), nullable=False)

class Actividad(Base):
    __tablename__ = 'actividad'
    cod_actividad = Column(CHAR(10), primary_key=True)
    nombre_actividad = Column(CHAR(50), nullable=False)
    descripcion = Column(String(30), nullable=False)
    fecha_inicio_actividad = Column(Date, nullable=False)
    fecha_fin_actividad = Column(Date, nullable=False)
    costo_actividad = Column(Numeric(5, 2), nullable=False)
    estado_actividad = Column(String(10), nullable=False)
    id_proyecto = Column(CHAR(10), ForeignKey('proyecto_recobro.id_proyecto'), nullable=False)

class PersonaEmail(Base):
    __tablename__ = 'persona_email'
    email = Column(String(50), primary_key=True)
    id_persona = Column(CHAR(10), ForeignKey('persona.id_persona'), primary_key=True)

class PersonaTelefono(Base):
    __tablename__ = 'persona_telefono'
    telefono = Column(Integer, primary_key=True)
    id_persona = Column(CHAR(10), ForeignKey('persona.id_persona'), primary_key=True)

class Prioridad(Base):
    __tablename__ = 'prioridad'
    prioridad = Column(CHAR(2), primary_key=True)
    descrip_prioridad = Column(String(64), nullable=False)

class Instalacion(Base):
    __tablename__ = 'instalacion'
    id_instalacion = Column(CHAR(6), primary_key=True)
    nombre_instalacion = Column(String(40), nullable=False)
    id_zona = Column(CHAR(5), ForeignKey('zona.id_zona'), nullable=False)

class EspacioComercial(Base):
    __tablename__ = 'espacio_comercial'
    id_espacio_comercial = Column(CHAR(10), primary_key=True)
    tipo_inmueble = Column(String(10), nullable=False)
    estado = Column(String(10), nullable=False)
    area = Column(Numeric(6, 2), nullable=False)
    tarifa = Column(Numeric(6, 2), nullable=False)
    id_zona = Column(CHAR(5), ForeignKey('zona.id_zona'), nullable=False)

class Inquilino(Base):
    __tablename__ = 'inquilino'
    id_inquilino = Column(CHAR(10), primary_key=True)
    razon_social = Column(String(50), nullable=False)
    fecha_eliminacion = Column(Date)
    fecha_registro = Column(Date, nullable=False)
    estado_inquilino = Column(estado_inquilino, nullable=False)
    id_persona = Column(CHAR(10), ForeignKey('persona.id_persona'), nullable=False)
    id_espacio_comercial = Column(CHAR(10), ForeignKey('espacio_comercial.id_espacio_comercial'), nullable=False)

class EspacioComun(Base):
    __tablename__ = 'espacio_comun'
    id_espacio_comun = Column(CHAR(10), primary_key=True)
    estado = Column(estado_espacio_comun, nullable=False)
    area = Column(Float, nullable=False)
    precio_por_dia = Column(Float, nullable=False)
    motivo_de_uso = Column(String(100), nullable=False)
    id_zona = Column(CHAR(5), ForeignKey('zona.id_zona'), nullable=False)

class Factura(Base):
    __tablename__ = 'factura'
    id_factura = Column(CHAR(10), primary_key=True)
    estado_factura = Column(estado_factura, nullable=False)
    fecha_emision = Column(Date, nullable=False)
    monto_total = Column(Float, nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    id_inquilino = Column(CHAR(10), ForeignKey('inquilino.id_inquilino'), nullable=False)

class Recordatorio(Base):
    __tablename__ = 'recordatorio'
    id_recordatorio = Column(CHAR(10), primary_key=True)
    tipo_recordatorio = Column(tipo_recordatorio, nullable=False)
    fecha_envio = Column(Date, nullable=False)
    contenido = Column(String(50), nullable=False)
    id_factura = Column(CHAR(10), ForeignKey('factura.id_factura'), nullable=False)

class Pago(Base):
    __tablename__ = 'pago'
    id_pago = Column(CHAR(10), primary_key=True)
    fecha_pago = Column(Date, nullable=False)
    metodo_pago = Column(metodo_pago, nullable=False)
    monto_pago = Column(Float, nullable=False)
    tipo_moneda = Column(String(10), nullable=False)
    id_factura = Column(CHAR(10), ForeignKey('factura.id_factura'), nullable=False)

class Evento(Base):
    __tablename__ = 'evento'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre_evento = Column(CHAR(50), unique=True, nullable=False)
    descripcion = Column(String(100), nullable=False)
    categoria = Column(String(100), nullable=False)
    objetivo = Column(String(50), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    id_espacio_comun = Column(CHAR(10), ForeignKey('espacio_comun.id_espacio_comun'), nullable=False)
    id_inquilino = Column(CHAR(10), ForeignKey('inquilino.id_inquilino'), nullable=False)

class RegistroIncidencia(Base):
    __tablename__ = 'registro_incidencia'
    cod_incidencia = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100), nullable=False)
    fecha_hora_registro = Column(Date, nullable=False)
    estado = Column(estado_incidencia, default='Pendiente')
    id_instalacion = Column(CHAR(6), ForeignKey('instalacion.id_instalacion'), nullable=False)
    id_empleado = Column(CHAR(10), ForeignKey('empleado.id_empleado'), nullable=False)

class ProgramMantenimiento(Base):
    __tablename__ = 'program_mantenimiento'
    dod_mantenimiento = Column(Integer, primary_key=True, autoincrement=True)
    plazo = Column(Date, nullable=False)
    descripcion = Column(String(100), nullable=False)
    estado = Column(estado_mantenimiento, default='Pendiente')
    id_instalacion = Column(CHAR(6), ForeignKey('instalacion.id_instalacion'), nullable=False)
    id_encargado = Column(CHAR(10), ForeignKey('empleado.id_empleado'), nullable=False)
    prioridad = Column(CHAR(2), ForeignKey('prioridad.prioridad'), nullable=False)
    cod_incidencia = Column(Integer, ForeignKey('registro_incidencia.cod_incidencia'))

class AcuerdoRecobro(Base):
    __tablename__ = 'acuerdo_recobro'
    id_acuerdo = Column(CHAR(10), primary_key=True)
    fecha_acuerdo = Column(Date, nullable=False)
    descripcion_acuerdo = Column(String(40), nullable=False)
    precio_acuerdo = Column(Integer, nullable=False)
    id_proyecto = Column(CHAR(10), ForeignKey('proyecto_recobro.id_proyecto'), nullable=False)
    id_factura = Column(CHAR(10), ForeignKey('factura.id_factura'), nullable=False)

class ContratoAlquiler(Base):
    __tablename__ = 'contrato_alquiler'
    id_contrato = Column(CHAR(10), primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    monto = Column(Numeric(10, 2), nullable=False)
    condicion = Column(String(256), nullable=False)
    fecha_vencimiento = Column(Date, nullable=False)
    estado = Column(estado_contrato_alquiler, nullable=False)
    porcentaje = Column(Numeric(5, 2), nullable=False)
    id_documento = Column(CHAR(10), ForeignKey('documento.id_documento'), nullable=False)
    id_factura = Column(CHAR(10), ForeignKey('factura.id_factura'), nullable=False)
    id_espacio_comercial = Column(CHAR(10), ForeignKey('espacio_comercial.id_espacio_comercial'), nullable=False)

class RegistroMantenimiento(Base):
    __tablename__ = 'registro_mantenimiento'
    cod_r_mantenimiento = Column(Integer, primary_key=True, autoincrement=True)
    observaciones = Column(String(64))
    fecha_realizada = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    id_instalacion = Column(CHAR(6), ForeignKey('instalacion.id_instalacion'), nullable=False)
    dod_mantenimiento = Column(Integer, ForeignKey('program_mantenimiento.dod_mantenimiento'), nullable=False)
    id_empleado = Column(CHAR(10), ForeignKey('empleado.id_empleado'), nullable=False)