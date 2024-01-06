use biblioteca;

CREATE TABLE Autores (
    AutorID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Nacionalidad VARCHAR(50)
);


CREATE TABLE Usuarios (
    UsuarioID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Email VARCHAR(100)
);

CREATE TABLE Libros (
    LibroID INT PRIMARY KEY,
    Titulo VARCHAR(100),
    AutorID INT,
    ISBN VARCHAR(13),
    Prestado BOOLEAN,
    UsuarioID INT,
    FOREIGN KEY (AutorID) REFERENCES Autores(AutorID),
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
);