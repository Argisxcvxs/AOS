-- Inserción de datos en la tabla de Autores
INSERT INTO Autores (AutorID, Nombre, Nacionalidad) VALUES
(1, 'Gabriel Garcia Marquez', 'Colombiano'),
(2, 'J.K. Rowling', 'Británico'),
(3, 'Haruki Murakami', 'Japonés');

-- Inserción de datos en la tabla de Usuarios
INSERT INTO Usuarios (UsuarioID, Nombre, Email) VALUES
(1, 'Carlos', 'carlos@email.com'),
(2, 'Ana', 'ana@email.com');

-- Inserción de datos en la tabla de Libros
INSERT INTO Libros (LibroID, Titulo, AutorID, ISBN, Prestado, UsuarioID) VALUES
(101, 'Cien años de soledad', 1, '978-0307350485', false, NULL),
(102, 'Harry Potter y la piedra filosofal', 2, '978-8498386264', true, 1),
(103, 'Norwegian Wood', 3, '978-0375704024', false, NULL);


INSERT INTO Autores (AutorID, Nombre, Nacionalidad) VALUES
(4, 'Jane Austen', 'Británico'),
(5, 'Mario Vargas Llosa', 'Peruano'),
(6, 'Agatha Christie', 'Británico');

INSERT INTO Usuarios (UsuarioID, Nombre, Email) VALUES
(3, 'Laura', 'laura@email.com'),
(4, 'Juan', 'juan@email.com');


INSERT INTO Libros (LibroID, Titulo, AutorID, ISBN, Prestado, UsuarioID) VALUES
(104, 'Orgullo y prejuicio', 4, '978-1613823721', false, NULL),
(105, 'La ciudad y los perros', 5, '978-8466304778', false, NULL),
(106, 'Asesinato en el Orient Express', 6, '978-0062073501', true, 2),
(107, 'El coronel no tiene quien le escriba', 1, '978-1400034949', false, NULL);

