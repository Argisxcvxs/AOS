#1.
persona = input ("dijite su nombre:")
if type(persona == str):
    print("hola, ten un buen dia", persona)

#2.
numero = input("dijite su numero:")
operador = int(numero)

def funcion (operador):
    suma = (operador * (operador + 1)) / 2
    return  suma

resultado = funcion(operador)
print("La suma de los números es:", resultado)

#3.
import math

numero_a = input("Digite el valor del cateto a en centimetros: ")
numero_b = input("Digite el valor del cateto b en centimetros: ")
print("Recuerde que estos valores deben corresponder a un triángulo rectángulo")

cateto_a = int(numero_a)
cateto_b = int(numero_b)

def funcion_a(cateto_a):
    potencia_a = cateto_a ** 2
    return potencia_a

def funcion_b(cateto_b):
    potencia_b = cateto_b ** 2
    return potencia_b

suma = math.sqrt(funcion_a(cateto_a) + funcion_b(cateto_b))
print("La hipotenusa es:", suma)

#5
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el operador (+, -, *, /): ")

if operador == "+":
    resultado = sumar(num1, num2)
elif operador == "-":
    resultado = restar(num1, num2)
elif operador == "*":
    resultado = multiplicar(num1, num2)
elif operador == "/":
    resultado = dividir(num1, num2)
else:
    print("Operador no válido")

print("El resultado es:", resultado)

#6
def es_palindromo(cadena):
    
    cadena = cadena.replace(" ", "").lower()
    
    if cadena == cadena[::-1]:
        return True
    else:
        return False

cadena = input("Ingrese una palabra o frase: ")

if es_palindromo(cadena):
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")

7. 
numero_tabla = int(input("Ingrese el número de la tabla de multiplicar: "))
numeros = 10
def tabla(numero_tabla, numeros):
    for i in range(1, numeros+1):
        resultado = numero_tabla * i
        print(resultado)
tabla(numero_tabla, numeros)
