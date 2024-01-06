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


