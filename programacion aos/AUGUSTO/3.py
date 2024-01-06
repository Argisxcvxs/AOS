#3
numero = int(input("Ingrese un número para escribir la tabla de multiplicar: ")) #se ingresa el numero con el que se hara la tabla de multiplicar

for i in range(1, 11): #se multiplican los numeros entre si en unrango de 1 a 10 atraves de la variable i y luego se imprimen
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")