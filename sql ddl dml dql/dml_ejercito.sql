INSERT INTO Cuerpos (codigo_cuerpo, denominacion) VALUES
    (1, 'Infantería'),
    (2, 'Artillería'),
    (3, 'Armada');
    
INSERT INTO Cuarteles (codigo_cuartel, nombre_cuartel, ubicacion) VALUES
    (101, 'Cuartel Central', 'Ubicación Central'),
    (102, 'Cuartel Norte', 'Ubicación Norte'),
    (103, 'Cuartel Sur', 'Ubicación Sur');
    
INSERT INTO Companias (numero_compania, actividad_principal) VALUES
    (1, 'Patrullaje'),
    (2, 'Artillería Pesada'),
    (3, 'Navegación');
    
INSERT INTO Soldados (codigo_soldado, nombre, apellidos, grado, codigo_cuerpo1, numero_compania1, codigo_cuartel1) VALUES
    (1001, 'Juan', 'Pérez', 'Cabo', 1, 1, 101),
    (1002, 'Ana', 'Gómez', 'Sargento', 2, 2, 101),
    (1003, 'Carlos', 'Rodríguez', 'Soldado', 3, 3, 102);
    
INSERT INTO Servicios (codigo_servicio, actividad) VALUES
    (301, 'Guardia'),
    (302, 'Cuartelero'),
    (303, 'Patrullaje Nocturno');
    
--
INSERT INTO Soldados_Servicios (codigo_soldado1, codigo_servicio1, fecha_realizacion) VALUES
    (1001, 301, '2023-01-15'),
    (1002, 302, '2023-02-20'),
    (1003, 303, '2023-03-10');
    
INSERT INTO Cuarteles_Companias (numero_compania1, codigo_cuartel1) VALUES
(1, 101),
(2, 102),
(3, 103);


INSERT INTO Cuerpos (codigo_cuerpo, denominacion) VALUES
    (4, 'Caballería'),
    (5, 'Fuerza Aérea');
    
INSERT INTO Cuarteles (codigo_cuartel, nombre_cuartel, ubicacion) VALUES
    (104, 'Cuartel Oeste', 'Ubicación Oeste'),
    (105, 'Cuartel Este', 'Ubicación Este');
    
INSERT INTO Companias (numero_compania, actividad_principal) VALUES
    (4, 'Exploración'),
    (5, 'Rescate');
    
INSERT INTO Soldados (codigo_soldado, nombre, apellidos, grado, codigo_cuerpo1, numero_compania1, codigo_cuartel1) VALUES
    (1004, 'Luisa', 'Fernández', 'Capitán', 4, 4, 104),
    (1005, 'Miguel', 'López', 'Teniente', 5, 5, 105);


INSERT INTO Servicios (codigo_servicio, actividad) VALUES
    (304, 'Vigilancia'),
    (305, 'Entrenamiento'),
    (306, 'Mantenimiento de Equipos');


INSERT INTO Soldados_Servicios (codigo_soldado1, codigo_servicio1, fecha_realizacion) VALUES
    (1004, 304, '2023-04-05'),
    (1005, 305, '2023-05-12'),
    (1001, 306, '2023-06-20');
    

INSERT INTO Cuarteles_Companias (numero_compania1, codigo_cuartel1) VALUES
(4, 104),
(5, 105);

INSERT INTO Cuerpos (codigo_cuerpo, denominacion) 
VALUES
(6, 'Inteligencia'),
(7, 'Fuerzas Especiales');
    
INSERT INTO Cuarteles (codigo_cuartel, nombre_cuartel, ubicacion) VALUES
    (106, 'Cuartel Central Norte', 'Ubicación Central Norte'),
    (107, 'Cuartel Central Sur', 'Ubicación Central Sur');
    
INSERT INTO Companias (numero_compania, actividad_principal) VALUES
    (6, 'Recolección de Información'),
    (7, 'Operaciones Encubiertas');
    
INSERT INTO Soldados (codigo_soldado, nombre, apellidos, grado, codigo_cuerpo1, numero_compania1, codigo_cuartel1) VALUES
    (1006, 'Elena', 'Martínez', 'Mayor', 5, 4, 104),
    (1007, 'Héctor', 'Ramírez', 'Sargento Mayor', 7, 4, 105);
    
INSERT INTO Servicios (codigo_servicio, actividad) VALUES
    (307, 'Infiltración'),
    (308, 'Interrogatorio'),
    (309, 'Evaluación de Riesgos');
    
INSERT INTO Soldados_Servicios (codigo_soldado1, codigo_servicio1, fecha_realizacion) VALUES
    (1006, 307, '2023-07-10'),
    (1006, 308, '2023-08-15'),
    (1002, 309, '2023-09-25');
    
INSERT INTO Cuarteles_Companias (numero_compania1, codigo_cuartel1) VALUES
    (6, 106),
    (6, 107),
    (7, 107);







    
