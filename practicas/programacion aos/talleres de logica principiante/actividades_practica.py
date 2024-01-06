#1
compras = []  

contador = 0

while contador < 1:
    compra = input("Ingrese el nombre del producto:")
    compra = input("Ingrese el codigo del producto:")
    precio = input("Ingrese el precio por cantidad de productos:")
    compras.append(compra)  
    contador += 1

print("Se ha alcanzado el límite máximo de uso de la variable.")

total_precio = int(precio)

if total_precio < 100:
    print("compra exitosa")

elif total_precio > 100:
    descuento = total_precio * 0.1
    precio_con_descuento = total_precio - descuento  

    print("Precio original:", total_precio)
    print("Descuento:", descuento)
    print("Precio con descuento:", precio_con_descuento)



#2
    numero = int(input("Ingrese un número para escribir la tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#3
import time
numero = input("presione enter para generar un numero al azar")
print("tienes 10 segundos para adivinar el numero")
def cuenta_regresiva(tiempo):
    for i in range(tiempo, 0, -1):
        print(i)
        time.sleep(1)
    print("¡Tiempo finalizado!")

tiempo = int("10")
cuenta_regresiva(tiempo)

#4
tasa = 4.1
dolar = input("ingrese la cantidad de dolares:")
conversion = float(dolar)
print (conversion * tasa)