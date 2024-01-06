#7
numeros = int(input("ingrese varios numeros enteros para sumarlos entre si: ")) #recogemos los datos y los definimos como enteros
suma = 0 #variable para almacenar los valores  
for digito in numeros: #bucle que recorre todos los numeros de los datos en la variable dijito
    suma += int(digito) #se suma cada dijito en el bucle a la variable de suma
print("La suma de los digitos es:", suma) #se imprime la variable con todos los dijitos sumados