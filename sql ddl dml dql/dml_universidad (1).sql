-- Insertar estudiantes

INSERT INTO Estudiantes (Nombre, Edad, CorreoElectronico)
VALUES ('Juan Pérez', 20, 'juan@example.com'),
       ('María González', 22, 'maria@example.com'),
       ('Carlos Rodríguez', 21, 'carlos@example.com');
       
-- Insertar Cursos

INSERT INTO Cursos (NombreCurso)
VALUES ('Matemáticas'),
       ('Historia'),
       ('Programación');
       
-- Realizar inscripciones

-- Juan se inscribe en Matemáticas y Programación
INSERT INTO Inscripciones (EstudianteID, CursoID)
VALUES (1, 1),
       (1, 3);

-- María se inscribe en Historia
INSERT INTO Inscripciones (EstudianteID, CursoID)
VALUES (2, 2);

-- Carlos se inscribe en Programación
INSERT INTO Inscripciones (EstudianteID, CursoID)
VALUES (3, 3);

-- Insertar mas estudiantes
INSERT INTO Estudiantes (Nombre, Edad, CorreoElectronico)
VALUES ('Laura Martínez', 25, 'laura@example.com'),
       ('Pedro Ramírez', 19, 'pedro@example.com'),
       ('Ana Sánchez', 24, 'ana@example.com');
       
-- Insertar mas cursos
INSERT INTO Cursos (NombreCurso)
VALUES ('Inglés'),
       ('Ciencias'),
       ('Literatura');
       
-- Realizar mas inscripciones

-- Laura se inscribe en Inglés y Ciencias
INSERT INTO Inscripciones (EstudianteID, CursoID)
VALUES (4, 4),
       (4, 5);

-- Pedro se inscribe en Literatura
INSERT INTO Inscripciones (EstudianteID, CursoID)
VALUES (5, 6);

-- Ana se inscribe en Ciencias y Literatura
INSERT INTO Inscripciones (EstudianteID, CursoID)
VALUES (6, 5),
       (6, 6);