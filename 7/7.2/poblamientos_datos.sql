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

-- Poblamiento de datos
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
('P001', 'Nike', 123, 'Lima', 20123456789, 'RUC'),
('P002', 'Starbucks', 456, 'Arequipa', 20123456788, 'RUC'),
('P003', 'Adidas', 789, 'Cusco', 20123456787, 'RUC'),
('P004', 'Zara', 101, 'Trujillo', 20123456786, 'RUC'),
('P005', 'H&M', 112, 'Lima', 20123456785, 'RUC'),
('P006', 'Puma', 113, 'Piura', 20123456784, 'RUC'),
('P007', 'Levis', 114, 'Tacna', 20123456783, 'RUC'),
('P008', 'Apple', 115, 'Iquitos', 20123456782, 'RUC'),
('P009', 'Coca Cola', 116, 'Lima', 20123456781, 'RUC'),
('P010', 'Pepsi', 117, 'Lima', 20123456780, 'RUC'),
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
INSERT INTO Empleado (id_empleado, cargo, first_last_name, second_last_name, fecha_nacimiento, id_persona, id_contrato_empleado)
VALUES
('E001', 'Gerente', 'Pérez', 'González', '1985-05-15', 'P011', 'C001'),
('E002', 'Analista', 'Gómez', 'Mendoza', '1990-08-22', 'P012', 'C002'),
('E003', 'Asistente', 'López', 'Castañeda', '1995-11-30', 'P013', 'C003'),
('E004', 'Desarrollador', 'Martínez', 'Rojas', '1988-12-12', 'P014', 'C004'),
('E005', 'Diseñador', 'Fernández', 'Paredes', '1992-03-21', 'P015', 'C005'),
('E006', 'Contador', 'Hernández', 'Ríos', '1980-07-18', 'P016', 'C006'),
('E007', 'Técnico', 'Ramírez', 'Salazar', '1989-02-15', 'P017', 'C007'),
('E008', 'Gerente de Proyectos', 'Vargas', 'Martín', '1987-09-09', 'P018', 'C008'),
('E009', 'Vendedor', 'Sánchez', 'Acuña', '1993-04-14', 'P019', 'C009'),
('E010', 'Recepcionista', 'Torres', 'Gutiérrez', '1996-06-11', 'P020', 'C010');

-- Poblamiento de datos para Recobro
INSERT INTO Recobro (id_recobro, nombre_recobro, descripcion_recobro, razon_recobro, categoria_recobro, estado_recobro)
VALUES
('R001', 'Recobro1', 'Recobro por servicio', 'Deuda de servicio', 'Servicio', 'Pendiente'),
('R002', 'Recobro2', 'Recobro por alquiler', 'Deuda de alquiler', 'Alquiler', 'Enviado'),
('R003', 'Recobro3', 'Recobro por multa', 'Multa de tráfico', 'Multa', 'Ejecutado'),
('R004', 'Recobro4', 'Recobro por préstamo', 'Deuda de préstamo', 'Préstamo', 'Valorizando'),
('R005', 'Recobro5', 'Recobro por suministro', 'Deuda de suministro', 'Suministro', 'Completado'),
('R006', 'Recobro6', 'Recobro por servicio', 'Deuda de servicio', 'Servicio', 'Pendiente'),
('R007', 'Recobro7', 'Recobro por alquiler', 'Deuda de alquiler', 'Alquiler', 'Enviado'),
('R008', 'Recobro8', 'Recobro por multa', 'Multa de tráfico', 'Multa', 'Ejecutado'),
('R009', 'Recobro9', 'Recobro por préstamo', 'Deuda de préstamo', 'Préstamo', 'Valorizando'),
('R010', 'Recobro10', 'Recobro por suministro', 'Deuda de suministro', 'Suministro', 'Completado');

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
INSERT INTO Documento (id_documento, tipo_documento, fecha_subido)
VALUES
('D001', 'Factura', '2023-01-10'),
('D002', 'Contrato', '2023-02-15'),
('D003', 'Informe', '2023-03-20'),
('D004', 'Recibo', '2023-04-25'),
('D005', 'Presupuesto', '2023-05-30'),
('D006', 'Certificado', '2023-06-05'),
('D007', 'Informe Técnico', '2023-07-10'),
('D008', 'Acta', '2023-08-15'),
('D009', 'Propuesta', '2023-09-20'),
('D010', 'Otros', '2023-10-25');

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

-- Poblamiento de datos para Zona
INSERT INTO Zona (nombre_zona, piso, referencia)
VALUES
('Zona1', 1, 'Entrada Principal'),
('Zona2', 1, 'Cerca de la Escalera Mecánica'),
('Zona3', 1, 'Frente a la Tienda de Ropa'),
('Zona4', 2, 'Zona de Comidas Rápidas'),
('Zona5', 2, 'Cerca del Cine'),
('Zona6', 2, 'Área de Juguetes'),
('Zona7', 3, 'Terraza con Vista'),
('Zona8', 3, 'Cerca de la Zona de Entretenimiento'),
('Zona9', 3, 'Área de Electrónicos'),
('Zona10', 3, 'Cerca de la Salida de Emergencia');

-- Poblamiento de datos para Actividad
INSERT INTO Actividad (cod_actividad, descripcion, fecha_inicio, fecha_fin, id_proyecto)
VALUES
('A001', 'Reunión de equipo', '2023-01-01', '2023-01-01', 'P001'),
('A002', 'Entrega de informe', '2023-02-01', '2023-02-02', 'P002'),
('A003', 'Evaluación del proyecto', '2023-03-01', '2023-03-01', 'P003'),
('A004', 'Desarrollo de la aplicación', '2023-04-01', '2023-05-01', 'P004'),
('A005', 'Revisión de diseño', '2023-05-01', '2023-05-15', 'P005'),
('A006', 'Pruebas del sistema', '2023-06-01', '2023-06-10', 'P006'),
('A007', 'Lanzamiento del producto', '2023-07-01', '2023-07-01', 'P007'),
('A008', 'Capacitación al personal', '2023-08-01', '2023-08-01', 'P008'),
('A009', 'Monitoreo del proyecto', '2023-09-01', '2023-09-30', 'P009'),
('A010', 'Cierre del proyecto', '2023-10-01', '2023-10-10', 'P010');

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
INSERT INTO Espacio_Comercial (id_espacio_comercial, tipo_inmueble, estado, area, tarifa, nombre_zona)
VALUES
('EC001', 'Local', 'Disponible', 50.00, 500.00, 'Zona1'),
('EC002', 'Oficina', 'Ocupado', 100.00, 1500.00, 'Zona2'),
('EC003', 'Almacén', 'Disponible', 200.00, 1000.00, 'Zona3'),
('EC004', 'Tienda', 'Ocupado', 75.00, 700.00, 'Zona4'),
('EC005', 'Showroom', 'Disponible', 60.00, 800.00, 'Zona5'),
('EC006', 'Tienda', 'Ocupado', 90.00, 1200.00, 'Zona6'),
('EC007', 'Local', 'Disponible', 80.00, 650.00, 'Zona7'),
('EC008', 'Oficina', 'Ocupado', 110.00, 1600.00, 'Zona8'),
('EC009', 'Almacén', 'Disponible', 220.00, 1100.00, 'Zona9'),
('EC010', 'Tienda', 'Ocupado', 70.00, 900.00, 'Zona10');

-- Poblamiento de datos para Inquilino
INSERT INTO Inquilino (id_inquilino, razon_social, fecha_eliminacion, fecha_registro, estado_inquilino, id_persona, id_espacio_comercial)
VALUES
('I001', 'Nike S.A.', NULL, '2023-01-15', 'Activo', 'P001', 'EC001'),
('I002', 'Starbucks Corp.', NULL, '2023-02-20', 'Activo', 'P002', 'EC002'),
('I003', 'Adidas AG', NULL, '2023-03-25', 'Inactivo', 'P003', 'EC003'),
('I004', 'Zara SA', NULL, '2023-04-30', 'Activo', 'P004', 'EC004'),
('I005', 'H&M Group', NULL, '2023-05-05', 'Activo', 'P005', 'EC005'),
('I006', 'Puma SE', NULL, '2023-06-10', 'Inactivo', 'P006', 'EC006'),
('I007', 'Levis Strauss', NULL, '2023-07-15', 'Activo', 'P007', 'EC007'),
('I008', 'Apple Inc.', NULL, '2023-08-20', 'Activo', 'P008', 'EC008'),
('I009', 'Coca Cola Company', NULL, '2023-09-25', 'Inactivo', 'P009', 'EC009'),
('I010', 'PepsiCo, Inc.', NULL, '2023-10-30', 'Activo', 'P010', 'EC010');

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
INSERT INTO Pago (id_pago, fecha_pago, metodo_pago, monto_pago, tipo_moneda, id_factura)
VALUES
('P001', '2023-01-15', 'Manual', 100.00, 'S/.', 'F001'),
('P002', '2023-02-20', 'Automatico', 150.00, 'S/.', 'F002'),
('P003', '2023-03-25', 'Manual', 200.00, 'S/.', 'F003'),
('P004', '2023-04-30', 'Automatico', 250.00, 'S/.', 'F004'),
('P005', '2023-05-05', 'Manual', 300.00, 'S/.', 'F005'),
('P006', '2023-06-10', 'Automatico', 350.00, 'S/.', 'F006'),
('P007', '2023-07-15', 'Manual', 400.00, 'S/.', 'F007'),
('P008', '2023-08-20', 'Automatico', 450.00, 'S/.', 'F008'),
('P009', '2023-09-25', 'Manual', 500.00, 'S/.', 'F009'),
('P010', '2023-10-30', 'Automatico', 550.00, 'S/.', 'F010');

-- Poblamiento de datos para Evento
INSERT INTO Evento (codigo_evento, id_espacio_comun, id_inquilino, nombre_evento, descripcion, fecha_inicio, fecha_fin)
VALUES
('202400013', 'EC001', 'I001', 'Evento1', 'Conferencia sobre tecnología', '2023-01-10', '2023-01-10'),
('202400014', 'EC002', 'I002', 'Evento2', 'Taller de marketing', '2023-02-15', '2023-02-15'),
('202400015', 'EC003', 'I003', 'Evento3', 'Reunión de proyecto', '2023-03-20', '2023-03-20'),
('202400016', 'EC004', 'I004', 'Evento4', 'Seminario de ventas', '2023-04-25', '2023-04-25'),
('202400017', 'EC005', 'I005', 'Evento5', 'Capacitación de personal', '2023-05-30', '2023-05-30'),
('202400018', 'EC006', 'I006', 'Evento6', 'Presentación de resultados', '2023-06-05', '2023-06-05'),
('202400019', 'EC007', 'I007', 'Evento7', 'Taller de innovación', '2023-07-10', '2023-07-10'),
('202400020', 'EC008', 'I008', 'Evento8', 'Feria de negocios', '2023-08-15', '2023-08-15'),
('202400021', 'EC009', 'I009', 'Evento9', 'Exposición de productos', '2023-09-20', '2023-09-20'),
('202400022', 'EC010', 'I010', 'Evento10', 'Cierre de proyecto', '2023-10-25', '2023-10-25');

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
INSERT INTO Contrato_Alquiler (id_contrato, fecha_inicio, monto, condicion, fecha_vencimiento, estado, porcentaje, id_documento, id_factura, id_espacio_comercial)
VALUES
('CA001', '2023-01-01', 500.00, 'Mensual', '2024-01-01', 'Activo', 5.00, 'D001', 'F001', 'EC001'),
('CA002', '2023-02-01', 600.00, 'Mensual', '2024-02-01', 'Activo', 4.50, 'D002', 'F002', 'EC002'),
('CA003', '2023-03-01', 700.00, 'Mensual', '2024-03-01', 'Activo', 4.00, 'D003', 'F003', 'EC003'),
('CA004', '2023-04-01', 800.00, 'Mensual', '2024-04-01', 'Activo', 3.50, 'D004', 'F004', 'EC004'),
('CA005', '2023-05-01', 900.00, 'Mensual', '2024-05-01', 'Activo', 3.00, 'D005', 'F005', 'EC005'),
('CA006', '2023-06-01', 1000.00, 'Mensual', '2024-06-01', 'Activo', 2.50, 'D006', 'F006', 'EC006'),
('CA007', '2023-07-01', 1100.00, 'Mensual', '2024-07-01', 'Activo', 2.00, 'D007', 'F007', 'EC007'),
('CA008', '2023-08-01', 1200.00, 'Mensual', '2024-08-01', 'Activo', 1.50, 'D008', 'F008', 'EC008'),
('CA009', '2023-09-01', 1300.00, 'Mensual', '2024-09-01', 'Activo', 1.00, 'D009', 'F009', 'EC009'),
('CA010', '2023-10-01', 1400.00, 'Mensual', '2024-10-01', 'Activo', 0.50, 'D010', 'F010', 'EC010');

-- Poblamiento de datos para Registro_de_incidencia
INSERT INTO Registro_de_incidencia (cod_incidencia, descripcion, fecha_registro, hora_registro, estado, nombre_instalacion, dod_mantenimiento, id_empleado)
VALUES
('I001', 'Incidencia en el aire acondicionado', '2023-01-05', '2023-01-05 10:00:00', 'Pendiente', 'Zona de comidas', 'PM001', 'E001'),
('I002', 'Fuga de agua en el baño', '2023-02-10', '2023-02-10 11:00:00', 'Programado', 'Baño A', 'PM002', 'E002'),
('I003', 'Problemas con la iluminación', '2023-03-15', '2023-03-15 12:00:00', 'Pendiente', 'Tienda 2', 'PM003', 'E003'),
('I004', 'Ruido extraño en el ascensor', '2023-04-20', '2023-04-20 13:00:00', 'Programado', 'Zona comun', 'PM004', 'E004'),
('I005', 'Fugas en el sistema de calefacción', '2023-05-25', '2023-05-25 14:00:00', 'Pendiente', 'Estacionamiento', 'PM005', 'E005'),
('I006', 'Problema con la red eléctrica', '2023-06-30', '2023-06-30 15:00:00', 'Programado', 'Zona de tiendas', 'PM006', 'E006'),
('I007', 'Incidencia en el sistema de ventilación', '2023-07-05', '2023-07-05 16:00:00', 'Pendiente', 'Tienda 10', 'PM007', 'E007'),
('I008', 'Problemas de aire acondicionado', '2023-08-10', '2023-08-10 17:00:00', 'Programado', 'Zona de servicios', 'PM008', 'E008'),
('I009', 'Falla del sistema de las pantallas táctiles', '2023-09-15', '2023-09-15 18:00:00', 'Pendiente', 'Zona comun', 'PM009', 'E009'),
('I010', 'Problemas con la conexión de internet', '2023-10-20', '2023-10-20 19:00:00', 'Programado', 'Area de sistemas', 'PM010', 'E010');

-- Poblamiento de datos para Registro_Mantenimiento
INSERT INTO Registro_Mantenimiento (cod_r_mantenimiento, observaciones, fecha_realizada, hora_inicio, hora_fin, nombre, dod_mantenimiento, id_empleado)
VALUES
('RM001', 'Reemplazo de filtro de aire', '2023-01-10', '2023-01-10 09:00:00', '2023-01-10 10:00:00', 'Tienda 10', 'PM001', 'E001'),
('RM002', 'Ajuste de luces', '2023-02-15', '2023-02-15 10:00:00', '2023-02-15 11:00:00', 'Zona comun', 'PM002', 'E002'),
('RM003', 'Mantenimiento del sistema de ventilación', '2023-03-20', '2023-03-20 11:00:00', '2023-03-20 12:00:00', 'Zona comun', 'PM003', 'E003'),
('RM004', 'Reparación de goteras', '2023-04-25', '2023-04-25 12:00:00', '2023-04-25 13:00:00', 'Baño A', 'PM004', 'E004'),
('RM005', 'Revisión del sistema eléctrico', '2023-05-30', '2023-05-30 13:00:00', '2023-05-30 14:00:00', 'Estacionamiento', 'PM005', 'E005'),
('RM006', 'Cambio de bombillas', '2023-06-05', '2023-06-05 14:00:00', '2023-06-05 15:00:00', 'Zona de comidas', 'PM006', 'E006'),
('RM007', 'Mantenimiento de equipos de sonido', '2023-07-10', '2023-07-10 15:00:00', '2023-07-10 16:00:00', 'Zona de entretenimientos', 'PM007', 'E007'),
('RM008', 'Limpieza de alfombras', '2023-08-15', '2023-08-15 16:00:00', '2023-08-15 17:00:00', 'Zona comun', 'PM008', 'E008'),
('RM009', 'Revisión de sistemas de seguridad', '2023-09-20', '2023-09-20 17:00:00', '2023-09-20 18:00:00', 'Zona de servicios', 'PM009', 'E009'),
('RM010', 'Mantenimiento de aires acondicionados', '2023-10-25', '2023-10-25 18:00:00', '2023-10-25 19:00:00', 'Zona comun', 'PM010', 'E010');
