#1
serie_digitos = input("Ingrese la serie de dígitos separados por comas: ") #indica al ususario dijitar y como hacerlo
digitos = serie_digitos.split(",") #se separan los dijitos como elementos individuales y por comas

maximo = int(digitos[0]) #se crea una variable que contenga esta lista de dijitos separados iniciando por el primero y convirtiendolos en enteros

for digito in digitos: #empieza a crearse un bucle para que recorra cada elmento de la lista dijitos y se asignara el valor a la variable dijito
    if int(digito) > maximo: #se verifica el numero mas grande y se convierte en entero para la verificacion
        maximo = int(digito) #se definira el nuevo dijito mas grande

print("El número más grande es:", maximo) #imprimimos el dijito mas grande
#2
def fibonacci(n): #se define la funcion con el n que representa el numero de elementos en la serie
    if n <= 0: #si es menor o igual a 0 la serie no cuenta asi que sale vacia
        return []
    elif n == 1: #si es 1 la la lista sera 0 porque no hay multiplos que den otro valor
        return [0]
    elif n == 2: # si es 2 dara 0 y luego 1, estos son los primeros elementos de la serie
        return [0, 1]
    else: #Se utiliza un bucle while para calcular los términos de la serie de Fibonacci. El bucle se ejecuta mientras la longitud de la lista fibsea menor que n En cada iteración y se agrega a la lista fib la suma de los dos últimos elementos de la lista
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

n = int(input("Ingrese el número de elementos de la serie de Fibonacci que desea calcular: ")) #usamos la variable n para depositar los datos de hasta donde llegara la serie
resultado = fibonacci(n) #se define el resultado de la serie en una sola variable para imprimirla
print("La serie de Fibonacci es:", resultado)

#3
numero = int(input("Ingrese un número para escribir la tabla de multiplicar: ")) #se ingresa el numero con el que se hara la tabla de multiplicar

for i in range(1, 11): #se multiplican los numeros entre si en unrango de 1 a 10 atraves de la variable i y luego se imprimen
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")



#4 y 5
class user: #se define la clase a la que perteneceran los usuarios y se listan los datos que estaran en la funcion init con sus parametros
    def __init__(self, nombre, contraseña):
     self.nombre = nombre
     self.contraseña = contraseña
u1 = user("Augusto", "1234567A") #se crean los datos de ususarios con la clase user
u2 = user("Juanito", "1234567E")
usuario_invalido = 0  #variable que mantendra el bucle del menu de la calculadora mientras la variable sea 0
while usuario_invalido == 0:
   usuarios_en_lista = [u1, u2] #lista de usuarios
   usuario = input("dijite el nombre de usuario:") #dijitamos nuestras contraseñas y nombres para que sean evaluados y comparados en un bucle for en el rango que sera la lista de ususarios
   contraseña_dijitada = input("dijite su contraseña:")
   for i in range(len(usuarios_en_lista)):
      if usuarios_en_lista[i].nombre == usuario and usuarios_en_lista [i].contraseña == contraseña_dijitada: #se evalua si las congtraseñas corresponden a la lista
         print(usuarios_en_lista[i].nombre, "bienvenido al menu") #dentro de este condicional salimos del bucle si los datos corresponden permitiendo al usuario seguir con el programa 
         usuario_invalido = 1
         break
   if usuario_invalido == 0: # se define lo que pasara si los datos no corresponden, el usuario queda atrapado en el bucle
      print("intente nuevamente")
calculadora = 0 #definimos la variable con la que va a trabajar el bucle de la calculadora
while calculadora == 0:
    print("¿que desea hacer?(calculadora, salir del programa)") #se define un menu de opciones para la calculadora dentro de un bucle 
    calculadora = int(input("Si desea salir del programa, ingrese '1'. Si desea ejecutar la calculadora, ingrese '0': "))
    if calculadora == 1: #se define la condicion para salir del bucle y de la calculadora
        print("¡Vuelva pronto!")
        break
    operacion = input("Ingrese el nombre de la operación a realizar: ") #recogemos los datos para realizar las operaciones (tipo de operacion y numeros)
    numero1 = float(input("Ingrese el número 1: "))
    numero2 = float(input("Ingrese el número 2: "))
    suma = numero1 + numero2 # definimos en variables los tipos de operacion
    division = numero1 / numero2
    multiplicacion = numero1 * numero2
    if operacion == "suma": #definimos la condicion donde se realiza cada operacion dependiendo de la informacion que se ingrese
        resultado = suma
        print(resultado)
    elif operacion == "division":
        resultado = division
        print(resultado)
    elif operacion == "multiplicacion":
        resultado = multiplicacion
        print(resultado)
    else:
        print("Operación no válida") #parametro por si se recoge informacion que no corresponde a nada

#6
#definimos un usuario con nombre y con una cantidad de dinero en la lista para realizar las operaciones bancarias
usuario = ["EL PEPE", 20000] 
menu = 0
while menu == 0: #bucle que recorre todo el programa de operaciones abajo un menu con las opciones para el ususario, la accion que elija se guarda en la variable accion
    accion = input("¿Qué acción desea realizar?\n\
1. Retirar\n\
2. Consignar\n\
3. Consultar saldo\n\
4. Salir\n\
Digite aquí su elección: ") 
    if accion == "1": #definimos lo que pasara bajo cada condicion que el ususario puede elegir en cada condicion se hace un llamado a la la lista y a la ubicacion de la cantidad de dinero del usuario en la lista
        retiro = float(input("¿Cuánto desea retirar?: "))
        if retiro <= usuario[1]: #definimos la operacion y los nuevos datos de la lista despues de esta 
            usuario[1] -= retiro
            print("Su retiro fue exitoso") 
        else:
            print("Saldo insuficiente para realizar el retiro") #se ejecuta si no se cumple con la condicion de tener mas saldo de lo que se va a retirar
    elif accion == "2":
        nombre = input("Digite el nombre de la persona a la que va a consignar: ") #informacion de a quien se va a consignar
        consignacion = float(input("Digite la cantidad a consignar: "))#cantidad a consignar
        usuario[1] += consignacion #operacion y nuevo valor de variable despues de operar
        print("Consignación exitosa")
    elif accion == "3":
        print("Su saldo es:", usuario[1]) #imprime el valor del saldo en la lista de ususario
    elif accion == "4":
        print("Gracias por utilizar nuestros servicios") #imprime un final del programa al salir del bucle con la condicion de que el ususario tome la opccion 4
        break
    else:
        print("Opción no válida") #por si la opcion no esta dentro de los parametros del programa
    
    respuesta = input("¿Desea realizar otra acción? (si/no): ") #permite elegir al usuario si salir o no del bucle de todo el programa 
    if respuesta.lower() != "si": #define el texto a minusculas y si no es si el menu marcara un valor que parara el bucle
        menu = 1


#7
numeros = int(input("ingrese varios numeros enteros para sumarlos entre si: ")) #recogemos los datos y los definimos como enteros
suma = 0 #variable para almacenar los valores  
for digito in numeros: #bucle que recorre todos los numeros de los datos en la variable dijito
    suma += int(digito) #se suma cada dijito en el bucle a la variable de suma
print("La suma de los digitos es:", suma) #se imprime la variable con todos los dijitos sumados
#8
gastos_diarios = [] #lista para almacenar los datos de los gastos
gasto_total = 0
menu = 0
while menu == 0: #bucle que funcionara con la condicion de que menu se mantenga en 0 y abarcara todo el programa
    accion = input("¿Qué desea hacer?\n\
    1-consultar gasto diario\n\
    2-ingresar gastos de hoy\n\
    3-salir del programa\n\
    Digite aquí tu elección: ")#menu de opciones que estaran en la variable accion y definira las condiciones que se cumpliran

    if accion == "2": #bajo esta condicion entraremos en un pequeño bucle y habra un imnput para almacenar el gasto diario y añadirlo a la variable con .apppend como datos tipo float- decimales
        while True:
            gasto = input("Ingrese el gasto diario (o 'fin' para terminar): ")
            if gasto.lower() == "fin":
                break
            gastos_diarios.append(float(gasto))
            gasto_total += float(gasto)



    elif accion == "1":
        if len(gastos_diarios) == 0: #condicion por si la variable de datos es 0 se imprime un aviso
            print("No se han ingresado gastos aún.")
        else:#si la variable tiene una cantidad de gastos acumulados el bucle for la recorrera y para despues imprimir la variable dia formateando los valores de la variable i
            dia = 0
            for i in gastos_diarios:
                dia += 1
                print(f'Total Gasto dia {dia} = {i}')

    elif accion == "3": #accion que cambia la condicion del menu y nos saca del bucle finalizando el programa
       menu = 1
       print("Gracias por usar la calculadora de gastos")
       
    else:
       print("Opción inválida. Por favor, elija una opción válida.") #por si la opcion no esta en los parametros del programa



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