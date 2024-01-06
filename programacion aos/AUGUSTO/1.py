#1
serie_digitos = input("Ingrese la serie de dígitos separados por comas: ") #indica al ususario dijitar y como hacerlo
digitos = serie_digitos.split(",") #se separan los dijitos como elementos individuales y por comas

maximo = int(digitos[0]) #se crea una variable que contenga esta lista de dijitos separados iniciando por el primero y convirtiendolos en enteros

for digito in digitos: #empieza a crearse un bucle para que recorra cada elmento de la lista dijitos y se asignara el valor a la variable dijito
    if int(digito) > maximo: #se verifica el numero mas grande y se convierte en entero para la verificacion
        maximo = int(digito) #se definira el nuevo dijito mas grande

print("El número más grande es:", maximo) #imprimimos el dijito mas grande
