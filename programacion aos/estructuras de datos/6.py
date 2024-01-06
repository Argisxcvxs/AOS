class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print("Contacto agregado exitosamente.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None

    def editar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
                contacto.telefono = nuevo_telefono
                print("Contacto editado exitosamente.")
                return True
        return False

agenda = Agenda()

while True:
    print("----- Menú -----")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        contacto = Contacto(nombre, telefono)
        agenda.agregar_contacto(contacto)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        contacto = agenda.buscar_contacto(nombre)
        if contacto:
            print(contacto)
        else:
            print("Contacto no encontrado.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto a editar: ")
        if not agenda.editar_contacto(nombre):
            print("Contacto no encontrado.")
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
