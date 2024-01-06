class gen_info:
    def __init__(self):
        self.ventas = {"dia1": {}, "dia2": {}}

    def add_venta(self, dia, producto, cantidad):
        if producto in self.ventas[dia]:
            self.ventas[dia][producto] += cantidad
        else:
            self.ventas[dia][producto] = cantidad

    def total(self, dia):
        ventas_dia = self.ventas[dia]
        total_ventas = sum(ventas_dia.values())
        producto_mas_vendido = max(ventas_dia, key=ventas_dia.get)
        return total_ventas, producto_mas_vendido

mi = gen_info()

menu = 0
while menu == 0:
    print("bienvenido")
    menu2 = input("Por favor seleccione una opción:\n\
    1- Registrar ventas\n\
    2- recibir un informe de ventas\n\
    6- Salir del programa \n\
    SELECCIONE: ")
    if menu2 == "1":
        while True:
            menu_ventas = input("Por favor seleccione una opción:\n\
            1- ventas dia 1\n\
            2- ventas dia 2\n\
            3- volver al menú \n\
            SELECCIONE: ")

            if menu_ventas == "1":
                ventas1 = 0
                while ventas1 == 0:
                    print("Primer día de ventas")
                    print("--------------------")
                    for i in range(1, 4):
                        dia = "dia1"
                        producto = input("Ingrese el nombre del producto (digite salir para volver al menú): ")
                        if producto.lower() == "salir":
                            ventas1 = 1
                            break
                        cantidad = int(input("Ingrese la cantidad vendida: "))
                        mi.add_venta(dia, producto, cantidad)

            elif menu_ventas == "2":
                ventas2 = 0
                while ventas2 == 0:
                    print("\nSegundo día de ventas")
                    print("---------------------")
                    for i in range(1, 4):
                        dia = "dia2"
                        producto = input("Ingrese el nombre del producto (digite salir para volver al menú): ")
                        if producto.lower() == "salir":
                            ventas2 = 1
                            break
                        cantidad = int(input("Ingrese la cantidad vendida: "))
                        mi.add_venta(dia, producto, cantidad)
            else:
                break

    elif menu2 == "2":
        print("\nInforme de Ventas")
        print("-----------------")
        total_ventas_dia1, producto_dia1 = mi.total("dia1")
        total_ventas_dia2, producto_dia2 = mi.total("dia2")
        print(f"Total de ventas del día 1: {total_ventas_dia1}")
        print(f"Producto más vendido del día 1: {producto_dia1}")
        print(f"Total de ventas del día 2: {total_ventas_dia2}")
        print(f"Producto más vendido del día 2: {producto_dia2}")
    else:
        break
