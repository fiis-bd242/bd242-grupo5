--Eliminación de Tablas
DROP TABLE IF EXISTS Registro_Mantenimiento;
DROP TABLE IF EXISTS Registro_de_incidencia;
DROP TABLE IF EXISTS Contrato_Alquiler;
DROP TABLE IF EXISTS Acuerdo_recobro;
DROP TABLE IF EXISTS Program_Mantenimiento;
DROP TABLE IF EXISTS Evento;
DROP TABLE IF EXISTS Pago;
DROP TABLE IF EXISTS Recordatorio;
DROP TABLE IF EXISTS Factura;
DROP TABLE IF EXISTS Espacio_comun;
DROP TABLE IF EXISTS Inquilino;
DROP TABLE IF EXISTS Espacio_Comercial;
DROP TABLE IF EXISTS Instalacion;
DROP TABLE IF EXISTS Prioridad;
DROP TABLE IF EXISTS Persona_telefono;
DROP TABLE IF EXISTS Persona_email;
DROP TABLE IF EXISTS Actividad;
DROP TABLE IF EXISTS Zona;
DROP TABLE IF EXISTS Solicitud;
DROP TABLE IF EXISTS Documento;
DROP TABLE IF EXISTS Proyecto_recobro;
DROP TABLE IF EXISTS Recobro;
DROP TABLE IF EXISTS Empleado;
DROP TABLE IF EXISTS Persona;
DROP TABLE IF EXISTS Contrato_Empleado;

--Eliminación de los Types
DROP TYPE IF EXISTS estado_contrato;
DROP TYPE IF EXISTS jornada_laboral;
DROP TYPE IF EXISTS estado_recobro;
DROP TYPE IF EXISTS estado_proyecto;
DROP TYPE IF EXISTS estado_solicitud;
DROP TYPE IF EXISTS estado_inquilino;
DROP TYPE IF EXISTS estado_espacio_comun;
DROP TYPE IF EXISTS estado_factura;
DROP TYPE IF EXISTS tipo_recordatorio;
DROP TYPE IF EXISTS estado_mantenimiento;
DROP TYPE IF EXISTS estado_contrato_alquiler;
DROP TYPE IF EXISTS estado_incidencia;
DROP TYPE IF EXISTS tipo_instalacion;
DROP TYPE IF EXISTS metodo_pago;

-- Definición de tipos ENUM
CREATE TYPE estado_contrato AS ENUM ('Activo', 'Finalizado', 'Suspendido');
CREATE TYPE jornada_laboral AS ENUM ('Completa', 'Parcial', 'Turno rotativo');
CREATE TYPE estado_recobro AS ENUM ('Enviado', 'Valorizando', 'Pendiente', 'Ejecutado', 'Completado');
CREATE TYPE estado_proyecto AS ENUM ('Ejecutado', 'Supervision');
CREATE TYPE estado_solicitud AS ENUM ('Abierto', 'Cerrado');
CREATE TYPE estado_inquilino AS ENUM ('Activo', 'Inactivo');
CREATE TYPE estado_espacio_comun AS ENUM ('ocupado', 'disponible', 'mantenimiento');
CREATE TYPE estado_factura AS ENUM ('Pendiente', 'Pagado');
CREATE TYPE tipo_recordatorio AS ENUM ('Previo', 'Posterior');
CREATE TYPE estado_mantenimiento AS ENUM ('Pendiente', 'Hecho');
CREATE TYPE estado_contrato_alquiler AS ENUM ('Activo', 'Expirado', 'Renovado');
CREATE TYPE estado_incidencia AS ENUM ('Pendiente', 'Programado');
CREATE TYPE tipo_instalacion AS ENUM ('Zona', 'Tienda', 'Modulo');
CREATE TYPE metodo_pago AS ENUM ('Manual', 'Automatico');

--Creación de Tablas
CREATE TABLE Contrato_Empleado
(
  id_contrato_empleado CHAR(10) NOT NULL PRIMARY KEY,
  descripcion_cargo VARCHAR(50) NOT NULL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  estado_contrato estado_contrato NOT NULL,
  jornada_laboral jornada_laboral NOT NULL
);

CREATE TABLE Persona
(
  id_persona CHAR(10) NOT NULL PRIMARY KEY,
  nombre VARCHAR(15) NOT NULL,
  nro_domicilio INT NOT NULL,
  ciudad VARCHAR(30) NOT NULL,
  nro_documento VARCHAR(11) NOT NULL,
  tipo_documento VARCHAR(20) NOT NULL
);

CREATE TABLE Empleado
(
  id_empleado CHAR(10) NOT NULL PRIMARY KEY,
  cargo VARCHAR(50) NOT NULL,
  first_last_name VARCHAR(20) NOT NULL,
  second_last_name VARCHAR(20) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  id_persona CHAR(10) NOT NULL,
  id_contrato_empleado CHAR(10) NOT NULL,
  FOREIGN KEY (id_persona) REFERENCES Persona(id_persona),
  FOREIGN KEY (id_contrato_empleado) REFERENCES Contrato_Empleado(id_contrato_empleado)
);

CREATE TABLE Recobro
(
  id_recobro CHAR(10) NOT NULL PRIMARY KEY,
  nombre_recobro VARCHAR(20) NOT NULL,
  descripcion_recobro VARCHAR(50) NOT NULL,
  razon_recobro VARCHAR(30) NOT NULL,
  categoria_recobro VARCHAR(20) NOT NULL,
  estado_recobro estado_recobro NOT NULL
);

CREATE TABLE Proyecto_recobro
(
  id_proyecto CHAR(10) NOT NULL PRIMARY KEY,
  nombre_proyecto VARCHAR(30) NOT NULL,
  costos FLOAT NOT NULL,
  estado_proyecto estado_proyecto NOT NULL,
  fecha_inicio_proyecto DATE NOT NULL,
  fecha_fin_proyecto DATE NOT NULL,
  id_recobro CHAR(10) NOT NULL,
  FOREIGN KEY (id_recobro) REFERENCES Recobro(id_recobro)
);

CREATE TABLE Documento
(
  id_documento CHAR(10) NOT NULL PRIMARY KEY,
  tipo_documento VARCHAR(50) NOT NULL,
  fecha_subido DATE NOT NULL
);

CREATE TABLE Solicitud
(
  id_solicitud CHAR(10) NOT NULL PRIMARY KEY,
  estado_solicitud estado_solicitud NOT NULL,
  fecha_solicitud DATE NOT NULL,
  fecha_resolucion DATE NOT NULL,
  id_documento CHAR(10) NOT NULL,
  FOREIGN KEY (id_documento) REFERENCES Documento(id_documento)
);

CREATE TABLE Zona
(
  id_zona CHAR(5),
  piso INT NOT NULL,
  referencia VARCHAR(256) NOT NULL,
  nombre_zona VARCHAR(25) NOT NULL,
  PRIMARY KEY (id_zona)
);

CREATE TABLE Actividad
(
  cod_actividad CHAR(10) NOT NULL PRIMARY KEY,
  nombre_actividad CHAR(50) NOT NULL,
  descripcion VARCHAR(30) NOT NULL,
  fecha_inicio_actividad DATE NOT NULL,
  fecha_fin_actividad DATE NOT NULL,
  Costo_actividad Decimal(5,2) NOT NULL,
  Estado_actividad VARCHAR(10) NOT NULL,
  id_proyecto CHAR(10) NOT NULL,
  
  FOREIGN KEY (id_proyecto) REFERENCES Proyecto_recobro(id_proyecto)
);

CREATE TABLE Persona_email
(
  email VARCHAR(50) NOT NULL,
  id_persona CHAR(10) NOT NULL,
  PRIMARY KEY (email, id_persona),
  FOREIGN KEY (id_persona) REFERENCES Persona(id_persona)
);

CREATE TABLE Persona_telefono
(
  telefono INT NOT NULL,
  id_persona CHAR(10) NOT NULL,
  PRIMARY KEY (telefono, id_persona),
  FOREIGN KEY (id_persona) REFERENCES Persona(id_persona)
);

CREATE TABLE Prioridad
(
  prioridad CHAR(2) NOT NULL PRIMARY KEY,
  descrip_prioridad VARCHAR(64) NOT NULL
);

CREATE TABLE Instalacion
( 
  id_instalacion CHAR(6) not null,
  nombre_instalacion VARCHAR(40) NOT NULL,
  id_zona CHAR(5) NOT NULL,
  PRIMARY KEY (id_instalacion),
  FOREIGN KEY (id_zona) REFERENCES Zona(id_zona)
);

CREATE TABLE Espacio_Comercial
(
  id_espacio_comercial CHAR(10) NOT NULL PRIMARY KEY,
  tipo_inmueble VARCHAR(10) NOT NULL,
  estado VARCHAR(10) NOT NULL,
  area NUMERIC(6, 2) NOT NULL,
  tarifa NUMERIC(6, 2) NOT NULL,
  id_zona CHAR(5) NOT NULL,
  FOREIGN KEY (id_zona) REFERENCES Zona(id_zona)
);

CREATE TABLE Inquilino
(
  id_inquilino CHAR(10) NOT NULL PRIMARY KEY,
  razon_social VARCHAR(50) NOT NULL,
  fecha_eliminacion DATE,
  fecha_registro DATE NOT NULL,
  estado_inquilino estado_inquilino NOT NULL,
  id_persona CHAR(10) NOT NULL,
  id_espacio_comercial CHAR(10) NOT NULL,
  FOREIGN KEY (id_persona) REFERENCES Persona(id_persona),
  FOREIGN KEY (id_espacio_comercial) REFERENCES Espacio_Comercial(id_espacio_comercial)
);

CREATE TABLE Espacio_comun
(
  id_espacio_comun CHAR(10) NOT NULL PRIMARY KEY,
  estado estado_espacio_comun NOT NULL,
  area FLOAT NOT NULL,
  precio_por_dia FLOAT NOT NULL,
  motivo_de_uso VARCHAR(100) NOT NULL,
  id_zona CHAR(5) NOT NULL,
  FOREIGN KEY (id_zona) REFERENCES Zona(id_zona)
);

CREATE TABLE Factura
(
  id_factura CHAR(10) NOT NULL PRIMARY KEY,
  estado_factura estado_factura NOT NULL,
  fecha_emision DATE NOT NULL,
  monto_total FLOAT NOT NULL,
  fecha_vencimiento DATE NOT NULL,
  id_inquilino CHAR(10) NOT NULL,
  FOREIGN KEY (id_inquilino) REFERENCES Inquilino(id_inquilino)
);

CREATE TABLE Recordatorio
(
  id_recordatorio CHAR(10) NOT NULL PRIMARY KEY,
  tipo_recordatorio tipo_recordatorio NOT NULL,
  fecha_envio DATE NOT NULL,
  contenido VARCHAR(50) NOT NULL,
  id_factura CHAR(10) NOT NULL,
  FOREIGN KEY (id_factura) REFERENCES Factura(id_factura)
);

CREATE TABLE Pago
(
  id_pago CHAR(10) NOT NULL PRIMARY KEY,
  fecha_pago DATE NOT NULL,
  metodo_pago metodo_pago NOT NULL,
  monto_pago FLOAT NOT NULL,
  tipo_moneda VARCHAR(10) NOT NULL,
  id_factura CHAR(10) NOT NULL,
  FOREIGN KEY (id_factura) REFERENCES Factura(id_factura)
);

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE Evento
(
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  codigo_evento CHAR(20) UNIQUE NOT NULL,
  nombre_evento CHAR(50) NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  categoria VARCHAR(100) NOT NULL,
  objetivo VARCHAR(50) NOT NULL,
  fecha_inicio DATE NOT NULL,
  fecha_fin DATE NOT NULL,
  id_espacio_comun CHAR(10) NOT NULL,
  id_inquilino CHAR(10) NOT NULL,
  FOREIGN KEY (id_espacio_comun) REFERENCES Espacio_comun(id_espacio_comun),
  FOREIGN KEY (id_inquilino) REFERENCES Inquilino(id_inquilino)
);

CREATE TABLE Registro_de_incidencia
(
  cod_incidencia SERIAL NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  fecha_hora_registro TIMESTAMP NOT NULL,
  estado estado_incidencia default 'Pendiente',
  id_instalacion CHAR(6) NOT NULL,
  id_empleado CHAR(10) NOT NULL,
  PRIMARY KEY (cod_incidencia),
  FOREIGN KEY (id_instalacion) REFERENCES Instalacion(id_instalacion),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);

CREATE TABLE Program_Mantenimiento
(
  dod_mantenimiento SERIAL NOT NULL,
  plazo DATE NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  estado estado_mantenimiento default 'Pendiente',
  id_instalacion CHAR(6) NOT NULL,
  id_encargado CHAR(10) NOT NULL,
  prioridad CHAR(2) NOT NULL,
  cod_incidencia INTEGER,
  PRIMARY KEY (dod_mantenimiento),
  FOREIGN KEY (id_instalacion) REFERENCES Instalacion(id_instalacion),
  FOREIGN KEY (id_encargado) REFERENCES Empleado(id_empleado),
  FOREIGN KEY (prioridad) REFERENCES Prioridad(prioridad),
  foreign key (cod_incidencia) references Registro_de_incidencia(cod_incidencia)
);

CREATE TABLE Acuerdo_recobro
(
  id_acuerdo CHAR(10) NOT NULL PRIMARY KEY,
  fecha_acuerdo DATE NOT NULL,
  descripcion_acuerdo VARCHAR(40) NOT NULL,
  precio_acuerdo INT NOT NULL,
  id_proyecto CHAR(10) NOT NULL,
  id_factura CHAR(10) NOT NULL,
  FOREIGN KEY (id_proyecto) REFERENCES Proyecto_recobro(id_proyecto),
  FOREIGN KEY (id_factura) REFERENCES Factura(id_factura)
);

CREATE TABLE Contrato_Alquiler
(
  id_contrato CHAR(10) NOT NULL PRIMARY KEY,
  fecha_inicio DATE NOT NULL,
  monto NUMERIC(10, 2) NOT NULL,
  condicion VARCHAR(256) NOT NULL,
  fecha_vencimiento DATE NOT NULL,
  estado estado_contrato_alquiler NOT NULL,
  porcentaje NUMERIC(5, 2) NOT NULL,
  id_documento CHAR(10) NOT NULL,
  id_factura CHAR(10) NOT NULL,
  id_espacio_comercial CHAR(10) NOT NULL,
  FOREIGN KEY (id_documento) REFERENCES Documento(id_documento),
  FOREIGN KEY (id_factura) REFERENCES Factura(id_factura),
  FOREIGN KEY (id_espacio_comercial) REFERENCES Espacio_Comercial(id_espacio_comercial)
);

CREATE TABLE Registro_Mantenimiento
(
  cod_r_mantenimiento SERIAL NOT NULL,	
  observaciones VARCHAR(64),
  fecha_realizada DATE NOT NULL,
  hora_inicio TIME NOT NULL,
  hora_fin TIME NOT NULL,
  id_instalacion CHAR(6) NOT NULL,
  dod_mantenimiento INTEGER NOT NULL,
  id_empleado CHAR(10) NOT NULL,
  PRIMARY KEY (cod_r_mantenimiento),
  FOREIGN KEY (id_instalacion) REFERENCES Instalacion(id_instalacion),
  FOREIGN KEY (dod_mantenimiento) REFERENCES Program_Mantenimiento(dod_mantenimiento),
  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado)
);
