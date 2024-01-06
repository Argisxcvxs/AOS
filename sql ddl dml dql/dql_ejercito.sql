use ejercito_db_final;

-- Obtener el nombre, apellidos y denominación del cuerpo al que pertenece cada soldado
SELECT Soldados.nombre, Soldados.apellidos, Cuerpos.denominacion
FROM Soldados
INNER JOIN Cuerpos ON Soldados.codigo_cuerpo1 = Cuerpos.codigo_cuerpo;

select sold.nombre as nombre_soldado, sold.apellidos as apellido_soldado, cuerp.denominacion as denominacion_cuerpo
from Soldados as sold
inner join Cuerpos as cuerp ON sold.codigo_cuerpo1 = cuerp.codigo_cuerpo;


-- Obtener el nombre, apellidos y actividad principal de las compañías a las que están asignados los soldados. 
-- Mostrar también aquellos soldados que no están asignados a ninguna compañía.

SELECT Soldados.nombre, Soldados.apellidos, Companias.actividad_principal
FROM Soldados
LEFT JOIN Companias ON Soldados.numero_compania1 = Companias.numero_compania
WHERE Soldados.numero_compania1 IS NOT NULL;


-- Obtener el nombre del cuartel, su ubicación y la cantidad total de compañías asociadas a cada cuartel, 
-- incluso aquellos cuarteles que no tienen ninguna compañía asignada.

SELECT Cuarteles.nombre_cuartel, Cuarteles.ubicacion, COUNT(Companias.numero_compania) AS total_companias
FROM Cuarteles
RIGHT JOIN Cuarteles_Companias ON Cuarteles.codigo_cuartel = Cuarteles_Companias.codigo_cuartel1
LEFT JOIN Companias ON Cuarteles_Companias.numero_compania1 = Companias.numero_compania
GROUP BY Cuarteles.nombre_cuartel, Cuarteles.ubicacion;


-- Obtener el nombre, apellidos y actividad de los servicios realizados 
-- por los soldados que tienen el grado de "Sargento".

SELECT Soldados.nombre, Soldados.apellidos, Servicios.actividad, Soldados_Servicios.fecha_realizacion, Soldados.grado
FROM Soldados
JOIN Soldados_Servicios ON Soldados.codigo_soldado = Soldados_Servicios.codigo_soldado1
JOIN Servicios ON Soldados_Servicios.codigo_servicio1 = Servicios.codigo_servicio
WHERE Soldados.grado = 'Sargento';

-- inner join == join

-- Obtener la denominación del cuerpo y el número total de soldados en cada cuerpo. 
-- Mostrar únicamente cuerpos que tengan al menos un soldado asignado.

SELECT Cuerpos.denominacion as denominacion_cuerpo, COUNT(Soldados.codigo_soldado) AS total_soldados
FROM Cuerpos
INNER JOIN Soldados ON Cuerpos.codigo_cuerpo = Soldados.codigo_cuerpo1
GROUP BY Cuerpos.denominacion
HAVING COUNT(Soldados.codigo_soldado) > 0;

-- Obtener el nombre, apellidos y actividad de los servicios realizados por los soldados que pertenecen a la "Infantería". 
-- Mostrar los resultados ordenados por la fecha de realización en orden ascendente.
SELECT Soldados.nombre, Soldados.apellidos, Servicios.actividad, Soldados_Servicios.fecha_realizacion
FROM Soldados
JOIN Soldados_Servicios ON Soldados.codigo_soldado = Soldados_Servicios.codigo_soldado1
JOIN Servicios ON Soldados_Servicios.codigo_servicio1 = Servicios.codigo_servicio
JOIN Cuerpos ON Soldados.codigo_cuerpo1 = Cuerpos.codigo_cuerpo
WHERE Cuerpos.denominacion = 'Infantería'
ORDER BY Soldados_Servicios.fecha_realizacion ASC;


-- 1
-- Obtener el nombre y apellidos de todos los soldados, junto con la cantidad de servicios realizados por cada uno, 
-- incluso aquellos que no han realizado ningún servicio.

-- 2
-- Obtener la actividad principal de las compañías que tienen al menos dos cuarteles asociados.

































