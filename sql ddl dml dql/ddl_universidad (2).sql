CREATE DATABASE IF NOT EXISTS Universidad_3;
USE Universidad_3;

-- Crear la tabla estudiantes
CREATE TABLE IF NOT EXISTS Estudiantes (
    EstudianteID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Edad INT,
    CorreoElectronico VARCHAR(50)
);

-- Crear la tabla de cursos
CREATE TABLE IF NOT EXISTS Cursos (
    CursoID INT AUTO_INCREMENT PRIMARY KEY,
    NombreCurso VARCHAR(50) NOT NULL
);

-- Crear la tabla inscripciones
CREATE TABLE IF NOT EXISTS Inscripciones (
    InscripcionID INT AUTO_INCREMENT PRIMARY KEY,
    EstudianteID INT,
    CursoID INT
);