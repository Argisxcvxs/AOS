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