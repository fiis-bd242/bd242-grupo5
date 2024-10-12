--Regresar a estado original
TRUNCATE TABLE Registro_Mantenimiento;
TRUNCATE TABLE Registro_de_incidencia;
TRUNCATE TABLE Contrato_Alquiler;
TRUNCATE TABLE Acuerdo_recobro;
TRUNCATE TABLE Program_Mantenimiento;
TRUNCATE TABLE Evento;
TRUNCATE TABLE Pago;
TRUNCATE TABLE Recordatorio;
TRUNCATE TABLE Factura;
TRUNCATE TABLE Espacio_comun;
TRUNCATE TABLE Inquilino;
TRUNCATE TABLE Espacio_Comercial;
TRUNCATE TABLE Instalacion;
TRUNCATE TABLE Prioridad;
TRUNCATE TABLE Persona_telefono;
TRUNCATE TABLE Persona_email;
TRUNCATE TABLE Actividad;
TRUNCATE TABLE Zonas;
TRUNCATE TABLE Solicitud;
TRUNCATE TABLE Documento;
TRUNCATE TABLE Proyecto_recobro;
TRUNCATE TABLE Recobro;
TRUNCATE TABLE Empleado;
TRUNCATE TABLE Persona;
TRUNCATE TABLE Contrato_Empleado;

Select * from Evento;
--Poblamiento de datos
INSERT INTO Contrato_Empleado (id_contrato_empleado, descripcion_cargo, fecha_inicio, fecha_fin, estado_contrato, jornada_laboral)
VALUES
('C001', 'Gerente', '2023-01-01', '2024-01-07', 'Activo', 'Completa'),
('C002', 'Analista', '2023-02-01', '2024-02-08', 'Activo', 'Parcial'),
('C003', 'Asistente', '2023-03-01', '2024-03-04', 'Finalizado', 'Completa'),
('C004', 'Desarrollador', '2023-04-01', '2024-04-04', 'Activo', 'Turno rotativo'),
('C005', 'Diseñador', '2023-05-01', '2024-05-09', 'Suspendido', 'Parcial'),
('C006', 'Contador', '2023-06-01', '2024-06-02', 'Activo', 'Completa'),
('C007', 'Técnico', '2023-07-01', '2024-07-08', 'Activo', 'Turno rotativo'),
('C008', 'Gerente de Proyectos', '2023-08-08', '2024-08-01', 'Finalizado', 'Completa'),
('C009', 'Vendedor', '2023-09-01', '2024-09-07', 'Activo', 'Parcial'),
('C010', 'Recepcionista', '2023-10-01', '2024-10-05', 'Activo', 'Completa');

-- Poblamiento de datos para Persona
INSERT INTO Persona (id_persona, nombre, nro_domicilio, ciudad, nro_documento, tipo_documento)
VALUES
('P001', 'Nike', 123, 'Lima', 12345678, 'RUC'),
('P002', 'Starbucks', 456, 'Arequipa', 87654321, 'RUC'),
('P003', 'Adidas', 789, 'Cusco', 23456789, 'RUC'),
('P004', 'Zara', 101, 'Trujillo', 98765432, 'RUC'),
('P005', 'H&M', 112, 'Lima', 13579246, 'RUC'),
('P006', 'Puma', 113, 'Piura', 24681357, 'RUC'),
('P007', 'Levis', 114, 'Tacna', 36925814, 'RUC'),
('P008', 'Apple', 115, 'Iquitos', 85274136, 'RUC'),
('P009', 'Coca Cola', 116, 'Lima', 14725836, 'RUC'),
('P010', 'Pepsi', 117, 'Lima', 36925847, 'RUC'),
('P011', 'Juan', 118, 'Lima', 98765432, 'DNI'),
('P012', 'María', 119, 'Lima', 87654321, 'DNI'),
('P013', 'Pedro', 120, 'Lima', 23456789, 'DNI'),
('P014', 'Ana', 121, 'Lima', 13579246, 'DNI'),
('P015', 'Lucía', 122, 'Lima', 24681357, 'DNI'),
('P016', 'José', 123, 'Lima', 36925814, 'DNI'),
('P017', 'Diego', 124, 'Lima', 85274136, 'DNI'),
('P018', 'Sofía', 125, 'Lima', 14725836, 'DNI'),
('P019', 'Andrés', 126, 'Lima', 36925847, 'DNI'),
('P020', 'Carla', 127, 'Lima', 74185296, 'DNI');

-- Poblamiento de datos para Empleado
INSERT INTO Empleado (cargo, id_empleado, first_last_name, second_last_name, fecha_nacimiento, id_persona, id_contrato_empleado)
VALUES
('Gerente', 'E001', 'Pérez', 'González', '1985-05-15', 'P011', 'C001'),
('Analista', 'E002', 'Gómez', 'Mendoza', '1990-08-22', 'P012', 'C002'),
('Asistente', 'E003', 'López', 'Castañeda', '1995-11-30', 'P013', 'C003'),
('Desarrollador', 'E004', 'Martínez', 'Rojas', '1988-12-12', 'P014', 'C004'),
('Diseñador', 'E005', 'Fernández', 'Paredes', '1992-03-21', 'P015', 'C005'),
('Contador', 'E006', 'Hernández', 'Ríos', '1980-07-18', 'P016', 'C006'),
('Técnico', 'E007', 'Ramírez', 'Salazar', '1989-02-15', 'P017', 'C007'),
('Gerente de Proyectos', 'E008', 'Vargas', 'Martín', '1987-09-09', 'P018', 'C008'),
('Vendedor', 'E009', 'Sánchez', 'Acuña', '1993-04-14', 'P019', 'C009'),
('Recepcionista', 'E010', 'Torres', 'Gutiérrez', '1996-06-11', 'P020', 'C010');

-- Poblamiento de datos para Recobro
INSERT INTO Recobro (nombre_recobro, descripcion_recobro, id_recobro, razon_recobro, categoria_recobro, estado_recobro)
VALUES
('Recobro1', 'Recobro por servicio', 'R001', 'Deuda de servicio', 'Servicio', 'Pendiente'),
('Recobro2', 'Recobro por alquiler', 'R002', 'Deuda de alquiler', 'Alquiler', 'Enviado'),
('Recobro3', 'Recobro por multa', 'R003', 'Multa de tráfico', 'Multa', 'Ejecutado'),
('Recobro4', 'Recobro por préstamo', 'R004', 'Deuda de préstamo', 'Préstamo', 'Valorizando'),
('Recobro5', 'Recobro por suministro', 'R005', 'Deuda de suministro', 'Suministro', 'Completado'),
('Recobro6', 'Recobro por servicio', 'R006', 'Deuda de servicio', 'Servicio', 'Pendiente'),
('Recobro7', 'Recobro por alquiler', 'R007', 'Deuda de alquiler', 'Alquiler', 'Enviado'),
('Recobro8', 'Recobro por multa', 'R008', 'Multa de tráfico', 'Multa', 'Ejecutado'),
('Recobro9', 'Recobro por préstamo', 'R009', 'Deuda de préstamo', 'Préstamo', 'Valorizando'),
('Recobro10', 'Recobro por suministro', 'R010', 'Deuda de suministro', 'Suministro', 'Completado');

-- Poblamiento de datos para Proyecto_recobro
INSERT INTO Proyecto_recobro (id_proyecto, costos, estado_proyecto, nombre_proyecto, id_recobro)
VALUES
('P001', 1000.50, 'Ejecutado', 'Proyecto Alpha', 'R001'),
('P002', 1500.75, 'Supervision', 'Proyecto Beta', 'R002'),
('P003', 2000.00, 'Ejecutado', 'Proyecto Gamma', 'R003'),
('P004', 500.00, 'Supervision', 'Proyecto Delta', 'R004'),
('P005', 750.25, 'Ejecutado', 'Proyecto Epsilon', 'R005'),
('P006', 1200.40, 'Supervision', 'Proyecto Zeta', 'R006'),
('P007', 950.80, 'Ejecutado', 'Proyecto Eta', 'R007'),
('P008', 600.00, 'Supervision', 'Proyecto Theta', 'R008'),
('P009', 300.90, 'Ejecutado', 'Proyecto Iota', 'R009'),
('P010', 450.30, 'Supervision', 'Proyecto Kappa', 'R010');

-- Poblamiento de datos para Documento
INSERT INTO Documento (tipo_documento, id_documento, fecha_subido)
VALUES
('Factura', 'D001', '2023-01-10'),
('Contrato', 'D002', '2023-02-15'),
('Informe', 'D003', '2023-03-20'),
('Recibo', 'D004', '2023-04-25'),
('Presupuesto', 'D005', '2023-05-30'),
('Certificado', 'D006', '2023-06-05'),
('Informe Técnico', 'D007', '2023-07-10'),
('Acta', 'D008', '2023-08-15'),
('Propuesta', 'D009', '2023-09-20'),
('Otros', 'D010', '2023-10-25');

-- Poblamiento de datos para Solicitud
INSERT INTO Solicitud (id_solicitud, estado_solicitud, fecha_solicitud, fecha_resolucion, id_documento)
VALUES
('S001', 'Abierto', '2023-01-01', '2023-01-10', 'D001'),
('S002', 'Cerrado', '2023-02-01', '2023-02-10', 'D002'),
('S003', 'Abierto', '2023-03-01', '2023-03-10', 'D003'),
('S004', 'Cerrado', '2023-04-01', '2023-04-10', 'D004'),
('S005', 'Abierto', '2023-05-01', '2023-05-10', 'D005'),
('S006', 'Cerrado', '2023-06-01', '2023-06-10', 'D006'),
('S007', 'Abierto', '2023-07-01', '2023-07-10', 'D007'),
('S008', 'Cerrado', '2023-08-01', '2023-08-10', 'D008'),
('S009', 'Abierto', '2023-09-01', '2023-09-10', 'D009'),
('S010', 'Cerrado', '2023-10-01', '2023-10-10', 'D010');

-- Poblamiento de datos para Zonas
INSERT INTO Zonas (piso, referencia, nombre_zona)
VALUES
(1, 'Zona A', 'Zona1'),
(1, 'Zona B', 'Zona2'),
(2, 'Zona C', 'Zona3'),
(2, 'Zona D', 'Zona4'),
(3, 'Zona E', 'Zona5'),
(3, 'Zona F', 'Zona6'),
(4, 'Zona G', 'Zona7'),
(4, 'Zona H', 'Zona8'),
(5, 'Zona I', 'Zona9'),
(5, 'Zona J', 'Zona10');

-- Poblamiento de datos para Actividad
INSERT INTO Actividad (descripcion, cod_actividad, fecha_inicio, fecha_fin, id_proyecto)
VALUES
('Reunión de equipo', 'A001', '2023-01-01', '2023-01-01', 'P001'),
('Entrega de informe', 'A002', '2023-02-01', '2023-02-02', 'P002'),
('Evaluación del proyecto', 'A003', '2023-03-01', '2023-03-01', 'P003'),
('Desarrollo de la aplicación', 'A004', '2023-04-01', '2023-05-01', 'P004'),
('Revisión de diseño', 'A005', '2023-05-01', '2023-05-15', 'P005'),
('Pruebas del sistema', 'A006', '2023-06-01', '2023-06-10', 'P006'),
('Lanzamiento del producto', 'A007', '2023-07-01', '2023-07-01', 'P007'),
('Capacitación al personal', 'A008', '2023-08-01', '2023-08-01', 'P008'),
('Monitoreo del proyecto', 'A009', '2023-09-01', '2023-09-30', 'P009'),
('Cierre del proyecto', 'A010', '2023-10-01', '2023-10-10', 'P010');

-- Poblamiento de datos para Persona_email
INSERT INTO Persona_email (email, id_persona)
VALUES
('nike@example.com', 'P001'),
('starbucks@example.com', 'P002'),
('adidas@example.com', 'P003'),
('zara@example.com', 'P004'),
('hm@example.com', 'P005'),
('puma@example.com', 'P006'),
('levis@example.com', 'P007'),
('apple@example.com', 'P008'),
('cocacola@example.com', 'P009'),
('pepsi@example.com', 'P010'),
('juan.perez@example.com', 'P011'),
('maria.gomez@example.com', 'P012'),
('pedro.lopez@example.com', 'P013'),
('ana.martinez@example.com', 'P014'),
('lucia.fernandez@example.com', 'P015'),
('jose.hernandez@example.com', 'P016'),
('diego.ramirez@example.com', 'P017'),
('sofia.vargas@example.com', 'P018'),
('andres.sanchez@example.com', 'P019'),
('carla.torres@example.com', 'P020');

-- Poblamiento de datos para Persona_telefono
INSERT INTO Persona_telefono (telefono, id_persona)
VALUES
(123456789, 'P001'),
(987654321, 'P002'),
(456789123, 'P003'),
(321654987, 'P004'),
(654321789, 'P005'),
(147258369, 'P006'),
(258369147, 'P007'),
(369258147, 'P008'),
(741852963, 'P009'),
(963258741, 'P010'),
(951357852, 'P011'),
(753159486, 'P012'),
(852963741, 'P013'),
(159753486, 'P014'),
(456987321, 'P015'),
(321654987, 'P016'),
(789456123, 'P017'),
(654123789, 'P018'),
(321789456, 'P019'),
(987321654, 'P020');

-- Poblamiento de datos para Prioridad
INSERT INTO Prioridad (prioridad, descrip_prioridad)
VALUES
('I1', 'Baja'),
('I2', 'Media'),
('I3', 'Alta'),
('I4', 'Critica');

-- Poblamiento de datos para Instalacion
INSERT INTO Instalacion (nombre_instalacion, tipo, nombre_zona)
VALUES
('Zona de comidas', 'Zona', 'Zona1'),
('Zona de entretenimientos', 'Zona', 'Zona2'),
('Tienda 2', 'Tienda', 'Zona3'),
('Zona comun', 'Zona', 'Zona4'),
('Estacionamiento', 'Zona', 'Zona5'),
('Zona de tiendas', 'Zona', 'Zona6'),
('Tienda 10', 'Tienda', 'Zona7'),
('Zona de servicios', 'Zona', 'Zona8'),
('Area de sistemas', 'Zona', 'Zona9'),
('Baño A', 'Zona', 'Zona10');

-- Poblamiento de datos para Espacio_Comercial
INSERT INTO Espacio_Comercial (tipo_inmueble, estado, area, id_espacio_comercial, tarifa, nombre_zona)
VALUES
('Local', 'Disponible', 50.00, 'EC001', 500.00, 'Zona1'),
('Oficina', 'Ocupado', 100.00, 'EC002', 1500.00, 'Zona2'),
('Almacén', 'Disponible', 200.00, 'EC003', 1000.00, 'Zona3'),
('Tienda', 'Ocupado', 75.00, 'EC004', 700.00, 'Zona4'),
('Showroom', 'Disponible', 60.00, 'EC005', 800.00, 'Zona5'),
('Tienda', 'Ocupado', 90.00, 'EC006', 1200.00, 'Zona6'),
('Local', 'Disponible', 80.00, 'EC007', 650.00, 'Zona7'),
('Oficina', 'Ocupado', 110.00, 'EC008', 1600.00, 'Zona8'),
('Almacén', 'Disponible', 220.00, 'EC009', 1100.00, 'Zona9'),
('Tienda', 'Ocupado', 70.00, 'EC010', 900.00, 'Zona10');

-- Poblamiento de datos para Inquilino
INSERT INTO Inquilino (id_inquilino, fecha_eliminacion, fecha_registro, estado_inquilino, id_persona, id_espacio_comercial)
VALUES
('I001', NULL, '2023-01-15', 'Activo', 'P001', 'EC001'),
('I002', NULL, '2023-02-20', 'Activo', 'P002', 'EC002'),
('I003', NULL, '2023-03-25', 'Inactivo', 'P003', 'EC003'),
('I004', NULL, '2023-04-30', 'Activo', 'P004', 'EC004'),
('I005', NULL, '2023-05-05', 'Activo', 'P005', 'EC005'),
('I006', NULL, '2023-06-10', 'Inactivo', 'P006', 'EC006'),
('I007', NULL, '2023-07-15', 'Activo', 'P007', 'EC007'),
('I008', NULL, '2023-08-20', 'Activo', 'P008', 'EC008'),
('I009', NULL, '2023-09-25', 'Inactivo', 'P009', 'EC009'),
('I010', NULL, '2023-10-30', 'Activo', 'P010', 'EC010');

-- Poblamiento de datos para Espacio_comun
INSERT INTO Espacio_comun (id_espacio_comun, estado, area, precio_por_dia, motivo_de_uso, nombre_zona)
VALUES
('EC001', 'Disponible', 30.00, 15.00, 'Eventos', 'Zona1'),
('EC002', 'Ocupado', 40.00, 20.00, 'Reuniones', 'Zona2'),
('EC003', 'Disponible', 50.00, 25.00, 'Capacitaciones', 'Zona3'),
('EC004', 'Ocupado', 60.00, 30.00, 'Seminarios', 'Zona4'),
('EC005', 'Disponible', 70.00, 35.00, 'Conferencias', 'Zona5'),
('EC006', 'Ocupado', 80.00, 40.00, 'Talleres', 'Zona6'),
('EC007', 'Disponible', 90.00, 45.00, 'Eventos', 'Zona7'),
('EC008', 'Ocupado', 100.00, 50.00, 'Reuniones', 'Zona8'),
('EC009', 'Disponible', 110.00, 55.00, 'Capacitaciones', 'Zona9'),
('EC010', 'Ocupado', 120.00, 60.00, 'Seminarios', 'Zona10');

-- Poblamiento de datos para Factura
INSERT INTO Factura (id_factura, estado_factura, fecha_emision, monto_total, fecha_vencimiento, id_inquilino)
VALUES
('F001', 'Pendiente', '2023-01-10', 100.00, '2023-01-20', 'I001'),
('F002', 'Pagado', '2023-02-15', 150.00, '2023-02-25', 'I002'),
('F003', 'Pendiente', '2023-03-20', 200.00, '2023-03-30', 'I003'),
('F004', 'Pagado', '2023-04-25', 250.00, '2023-05-05', 'I004'),
('F005', 'Pendiente', '2023-05-30', 300.00, '2023-06-10', 'I005'),
('F006', 'Pagado', '2023-06-05', 350.00, '2023-06-15', 'I006'),
('F007', 'Pendiente', '2023-07-10', 400.00, '2023-07-20', 'I007'),
('F008', 'Pagado', '2023-08-15', 450.00, '2023-08-25', 'I008'),
('F009', 'Pendiente', '2023-09-20', 500.00, '2023-09-30', 'I009'),
('F010', 'Pagado', '2023-10-25', 550.00, '2023-11-05', 'I010');

-- Poblamiento de datos para Recordatorio
INSERT INTO Recordatorio (id_recordatorio, tipo_recordatorio, fecha_envio, contenido, id_factura)
VALUES
('R001', 'Previo', '2023-01-01', 'Recordatorio de pago', 'F001'),
('R002', 'Posterior', '2023-02-01', 'Factura vencida', 'F002'),
('R003', 'Previo', '2023-03-01', 'Recordatorio de pago', 'F003'),
('R004', 'Posterior', '2023-04-01', 'Factura vencida', 'F004'),
('R005', 'Previo', '2023-05-01', 'Recordatorio de pago', 'F005'),
('R006', 'Posterior', '2023-06-01', 'Factura vencida', 'F006'),
('R007', 'Previo', '2023-07-01', 'Recordatorio de pago', 'F007'),
('R008', 'Posterior', '2023-08-01', 'Factura vencida', 'F008'),
('R009', 'Previo', '2023-09-01', 'Recordatorio de pago', 'F009'),
('R010', 'Posterior', '2023-10-01', 'Factura vencida', 'F010');

-- Poblamiento de datos para Pago
INSERT INTO Pago (fecha_pago, id_pago, metodo_pago, monto_pago, tipo_moneda, id_factura)
VALUES
('2023-01-15', 'P001', 'Manual', 100.00, 'S/.', 'F001'),
('2023-02-20', 'P002', 'Automatico', 150.00, 'S/.', 'F002'),
('2023-03-25', 'P003', 'Manual', 200.00, 'S/.', 'F003'),
('2023-04-30', 'P004', 'Automatico', 250.00, 'S/.', 'F004'),
('2023-05-05', 'P005', 'Manual', 300.00, 'S/.', 'F005'),
('2023-06-10', 'P006', 'Automatico', 350.00, 'S/.', 'F006'),
('2023-07-15', 'P007', 'Manual', 400.00, 'S/.', 'F007'),
('2023-08-20', 'P008', 'Automatico', 450.00, 'S/.', 'F008'),
('2023-09-25', 'P009', 'Manual', 500.00, 'S/.', 'F009'),
('2023-10-30', 'P010', 'Automatico', 550.00, 'S/.', 'F010');

-- Poblamiento de datos para Evento
INSERT INTO Evento (nombre_evento, descripcion, fecha_inicio, fecha_fin, id_espacio_comun, id_inquilino)
VALUES
('Evento1', 'Conferencia sobre tecnología', '2023-01-10', '2023-01-10', 'EC001', 'I001'),
('Evento2', 'Taller de marketing', '2023-02-15', '2023-02-15', 'EC002', 'I002'),
('Evento3', 'Reunión de proyecto', '2023-03-20', '2023-03-20', 'EC003', 'I003'),
('Evento4', 'Seminario de ventas', '2023-04-25', '2023-04-25', 'EC004', 'I004'),
('Evento5', 'Capacitación de personal', '2023-05-30', '2023-05-30', 'EC005', 'I005'),
('Evento6', 'Presentación de resultados', '2023-06-05', '2023-06-05', 'EC006', 'I006'),
('Evento7', 'Taller de innovación', '2023-07-10', '2023-07-10', 'EC007', 'I007'),
('Evento8', 'Feria de negocios', '2023-08-15', '2023-08-15', 'EC008', 'I008'),
('Evento9', 'Exposición de productos', '2023-09-20', '2023-09-20', 'EC009', 'I009'),
('Evento10', 'Cierre de proyecto', '2023-10-25', '2023-10-25', 'EC010', 'I010');

-- Poblamiento de datos para Program_Mantenimiento
INSERT INTO Program_Mantenimiento (dod_mantenimiento, plazo, descripcion, estado, nombre_instalacion, id_administrador, prioridad)
VALUES
('PM001', '2023-01-01', 'Mantenimiento de equipos', 'Pendiente', 'Zona de comidas', 'E001', 'I1'),
('PM002', '2023-02-01', 'Revisión de sistema eléctrico', 'Hecho', 'Zona de entretenimientos', 'E002', 'I2'),
('PM003', '2023-03-01', 'Cambio de luces', 'Pendiente', 'Tienda 2', 'E003', 'I3'),
('PM004', '2023-04-01', 'Limpieza de filtros', 'Hecho', 'Zona comun', 'E004', 'I2'),
('PM005', '2023-05-01', 'Reparación de techos', 'Pendiente', 'Estacionamiento', 'E005', 'I1'),
('PM006', '2023-06-01', 'Inspección de instalaciones', 'Hecho', 'Zona de tiendas', 'E006', 'I1'),
('PM007', '2023-07-01', 'Mantenimiento preventivo', 'Pendiente', 'Tienda 10', 'E007', 'I3'),
('PM008', '2023-08-01', 'Reemplazo de equipos', 'Hecho', 'Zona de servicios', 'E008', 'I1'),
('PM009', '2023-09-01', 'Ajuste de sistemas', 'Pendiente', 'Area de sistemas', 'E009', 'I2'),
('PM010', '2023-10-01', 'Reparación de baños', 'Hecho', 'Baño A', 'E010', 'I1');

-- Poblamiento de datos para Acuerdo_recobro
INSERT INTO Acuerdo_recobro (id_acuerdo, fecha_acuerdo, descripcion_acuerdo, precio_acuerdo, id_proyecto, id_factura)
VALUES
('AR001', '2023-01-05', 'Acuerdo de pago por servicios', 1000, 'P001', 'F001'),
('AR002', '2023-02-10', 'Acuerdo de pago por alquiler', 1500, 'P002', 'F002'),
('AR003', '2023-03-15', 'Acuerdo de pago por multas', 200, 'P003', 'F003'),
('AR004', '2023-04-20', 'Acuerdo de pago por suministros', 500, 'P004', 'F004'),
('AR005', '2023-05-25', 'Acuerdo de pago por préstamo', 750, 'P005', 'F005'),
('AR006', '2023-06-30', 'Acuerdo de pago por servicios', 300, 'P006', 'F006'),
('AR007', '2023-07-05', 'Acuerdo de pago por alquiler', 1000, 'P007', 'F007'),
('AR008', '2023-08-10', 'Acuerdo de pago por multas', 150, 'P008', 'F008'),
('AR009', '2023-09-15', 'Acuerdo de pago por suministros', 800, 'P009', 'F009'),
('AR010', '2023-10-20', 'Acuerdo de pago por préstamo', 950, 'P010', 'F010');

-- Poblamiento de datos para Contrato_Alquiler
INSERT INTO Contrato_Alquiler (fecha_inicio, monto, condicion, id_contrato, fecha_vencimiento, estado, porcentaje, id_documento, id_factura, id_espacio_comercial)
VALUES
('2023-01-01', 500.00, 'Mensual', 'CA001', '2024-01-01', 'Activo', 5.00, 'D001', 'F001', 'EC001'),
('2023-02-01', 600.00, 'Mensual', 'CA002', '2024-02-01', 'Activo', 4.50, 'D002', 'F002', 'EC002'),
('2023-03-01', 700.00, 'Mensual', 'CA003', '2024-03-01', 'Activo', 4.00, 'D003', 'F003', 'EC003'),
('2023-04-01', 800.00, 'Mensual', 'CA004', '2024-04-01', 'Activo', 3.50, 'D004', 'F004', 'EC004'),
('2023-05-01', 900.00, 'Mensual', 'CA005', '2024-05-01', 'Activo', 3.00, 'D005', 'F005', 'EC005'),
('2023-06-01', 1000.00, 'Mensual', 'CA006', '2024-06-01', 'Activo', 2.50, 'D006', 'F006', 'EC006'),
('2023-07-01', 1100.00, 'Mensual', 'CA007', '2024-07-01', 'Activo', 2.00, 'D007', 'F007', 'EC007'),
('2023-08-01', 1200.00, 'Mensual', 'CA008', '2024-08-01', 'Activo', 1.50, 'D008', 'F008', 'EC008'),
('2023-09-01', 1300.00, 'Mensual', 'CA009', '2024-09-01', 'Activo', 1.00, 'D009', 'F009', 'EC009'),
('2023-10-01', 1400.00, 'Mensual', 'CA010', '2024-10-01', 'Activo', 0.50, 'D010', 'F010', 'EC010');

-- Poblamiento de datos para Registro_de_incidencia
INSERT INTO Registro_de_incidencia (descripcion, fecha_registro, hora_registro, cod_incidencia, estado, nombre_instalacion, dod_mantenimiento, id_empleado)
VALUES
('Incidencia en el aire acondicionado', '2023-01-05', '2023-01-05 10:00:00', 'I001', 'Pendiente', 'Zona de comidas', 'PM001', 'E001'),
('Fuga de agua en el baño', '2023-02-10', '2023-02-10 11:00:00', 'I002', 'Programado', 'Baño A', 'PM002', 'E002'),
('Problemas con la iluminación', '2023-03-15', '2023-03-15 12:00:00', 'I003', 'Pendiente', 'Tienda 2', 'PM003', 'E003'),
('Ruido extraño en el ascensor', '2023-04-20', '2023-04-20 13:00:00', 'I004', 'Programado', 'Zona comun', 'PM004', 'E004'),
('Fugas en el sistema de calefacción', '2023-05-25', '2023-05-25 14:00:00', 'I005', 'Pendiente', 'Estacionamiento', 'PM005', 'E005'),
('Problema con la red eléctrica', '2023-06-30', '2023-06-30 15:00:00', 'I006', 'Programado', 'Zona de tiendas', 'PM006', 'E006'),
('Incidencia en el sistema de ventilación', '2023-07-05', '2023-07-05 16:00:00', 'I007', 'Pendiente', 'Tienda 10', 'PM007', 'E007'),
('Problemas de aire acondicionado', '2023-08-10', '2023-08-10 17:00:00', 'I008', 'Programado', 'Zona de servicios', 'PM008', 'E008'),
('Falla del sistema de las pantallas tactiles', '2023-09-15', '2023-09-15 18:00:00', 'I009', 'Pendiente', 'Zona comun', 'PM009', 'E009'),
('Problemas con la conexión de internet', '2023-10-20', '2023-10-20 19:00:00', 'I010', 'Programado', 'Area de sistemas', 'PM010', 'E010');

-- Poblamiento de datos para Registro_Mantenimiento
INSERT INTO Registro_Mantenimiento (observaciones, cod_r_mantenimiento, fecha_realizada, hora_inicio, hora_fin, nombre, dod_mantenimiento, id_empleado)
VALUES
('Reemplazo de filtro de aire', 'RM001', '2023-01-10', '2023-01-10 09:00:00', '2023-01-10 10:00:00', 'Tienda 10', 'PM001', 'E001'),
('Ajuste de luces', 'RM002', '2023-02-15', '2023-02-15 10:00:00', '2023-02-15 11:00:00', 'Zona comun', 'PM002', 'E002'),
('Mantenimiento del sistema de ventilacion', 'RM003', '2023-03-20', '2023-03-20 11:00:00', '2023-03-20 12:00:00', 'Zona comun', 'PM003', 'E003'),
('Reparación de goteras', 'RM004', '2023-04-25', '2023-04-25 12:00:00', '2023-04-25 13:00:00', 'Baño A', 'PM004', 'E004'),
('Revisión de el sistema electrico', 'RM005', '2023-05-30', '2023-05-30 13:00:00', '2023-05-30 14:00:00', 'Estacionamiento', 'PM005', 'E005'),
('Cambio de bombillas', 'RM006', '2023-06-05', '2023-06-05 14:00:00', '2023-06-05 15:00:00', 'Zona de comidas', 'PM006', 'E006'),
('Mantenimiento de equipos de sonido', 'RM007', '2023-07-10', '2023-07-10 15:00:00', '2023-07-10 16:00:00', 'Zona de entretenimientos', 'PM007', 'E007'),
('Limpieza de alfombras', 'RM008', '2023-08-15', '2023-08-15 16:00:00', '2023-08-15 17:00:00', 'Zona comun', 'PM008', 'E008'),
('Revisión de sistemas de seguridad', 'RM009', '2023-09-20', '2023-09-20 17:00:00', '2023-09-20 18:00:00', 'Zona de servicios', 'PM009', 'E009'),
('Mantenimiento de aires acondicionados', 'RM010', '2023-10-25', '2023-10-25 18:00:00', '2023-10-25 19:00:00', 'Zona comun', 'PM010', 'E010');

