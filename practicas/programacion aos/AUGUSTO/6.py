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
