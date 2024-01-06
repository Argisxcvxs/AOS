#9
print("bienvenido") #imprimo un saludo
menu = 0
while menu == 0: #bucle que funciona solo si menu se mantiene en 0
    dinero = float(input("ingrese la cantidad de dinero:")) #se definen los valores a operar para calcular intereses como float y se recolectan en variables
    interes = float(input("ingrese el porcentaje de ineteres mensual(solo el numero):"))
    tiempo = float(input("ingrese el tiempo del prestamo en meses:"))
    porcentaje_interes = interes / 100 #se define una operacion con los datos almacenados en la variable interes para dar un numero que nos permita calcular un porcentaje
    calculo_interes = porcentaje_interes * tiempo * dinero #operacion de calculo de intereses definida en una variable
    print("el total de sus intereses es de:", calculo_interes) #imprime los intereses
    opcion = input("¿desea salir del programa?(si/no):") #opcion para salir del bucle cambiando la variable menu y saliendo de la condicion de bucle atraves de una comparacion de texto convertido a minusculas
    if opcion.lower() == "si":
        menu =1
        print("hasta luego") #se imprime una despedida