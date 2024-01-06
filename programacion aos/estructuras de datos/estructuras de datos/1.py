#diccionario del inventario
inventario = {
    'producto1': {'cantidad': 10, 'precio': 15.5},
    'producto2': {'cantidad': 5, 'precio': 20.0},
    'producto3': {'cantidad': 20, 'precio': 10.0}
}

#función para agregar un producto
def agregar_producto(inventario, producto, cantidad, precio):
    inventario[producto] = {'cantidad': cantidad, 'precio': precio}

#función para eliminar un producto
def eliminar_producto(inventario, producto):
    del inventario[producto]

#función para actualizar producto
def actualizar_producto(inventario, producto, cantidad=None, precio=None):
    if cantidad:
        inventario[producto]['cantidad'] = cantidad
    if precio:
        inventario[producto]['precio'] = precio

#menú
def menu():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Salir")
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        agregar_producto(inventario, producto, cantidad, precio)
        print("Producto agregado con éxito")

    elif opcion == '2':
        producto = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(inventario, producto)
        print("Producto eliminado con éxito")

    elif opcion == '3':
        producto = input("Ingrese el nombre del producto a actualizar: ")
        cantidad = input("Ingrese la nueva cantidad del producto (dejar vacío para mantener la misma cantidad): ")
        precio = input("Ingrese el nuevo precio del producto (dejar vacío para mantener el mismo precio): ")
        actualizar_producto(inventario, producto, cantidad, precio)
        print("Producto actualizado con éxito")

    elif opcion == '4':
        break

    else:
        print("Opción inválida")