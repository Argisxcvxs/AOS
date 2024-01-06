usuarios = {}
publicaciones = {}
usuarios_registrados = []

def registrar():
    nombre_usuario = input("Crea un nombre de usuario: ")
    contraseña = input("Crea una contraseña: ")
    usuarios[nombre_usuario] = {'nombre_usuario': nombre_usuario, 'contraseña': contraseña, 'seguidores': [], 'publicaciones': []}
    usuarios_registrados.append(nombre_usuario)
    print(f"¡Bienvenido, {nombre_usuario}! Te has registrado exitosamente.")

def iniciar_sesion():
    nombre_usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    if nombre_usuario in usuarios_registrados and usuarios[nombre_usuario]['contraseña'] == contraseña:
        print(f"¡Bienvenido de nuevo, {nombre_usuario}! Has iniciado sesión exitosamente.")
        menu_usuario(nombre_usuario)
    else:
        print("Nombre de usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

def menu_usuario(nombre_usuario):
    while True:
        print("\nMenú:")
        print("1. Seguir a un usuario")
        print("2. Ver tus publicaciones y las publicaciones de los usuarios que sigues")
        print("3. Crear una publicación")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            seguir_usuario(nombre_usuario)
        elif opcion == '2':
            ver_publicaciones(nombre_usuario)
        elif opcion == '3':
            crear_publicacion(nombre_usuario)
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, inténtalo de nuevo.")

def seguir_usuario(nombre_usuario):
    nombre_usuario_seguir = input("Ingresa el nombre de usuario del usuario que quieres seguir: ")
    if nombre_usuario_seguir in usuarios:
        usuarios[nombre_usuario]['seguidores'].append(nombre_usuario_seguir)
        print(f"Ahora estás siguiendo a {nombre_usuario_seguir}.")
    else:
        print("Este usuario no existe. Por favor, inténtalo de nuevo.")

def ver_publicaciones(nombre_usuario):
    print("\nTus publicaciones y las publicaciones de los usuarios que sigues:")
    for publicacion in publicaciones[nombre_usuario]:
        print(f"{publicacion['nombre_usuario']} - {publicacion['contenido']}")

def crear_publicacion(nombre_usuario):
    contenido = input("¿Qué quieres compartir? ")
    marca_tiempo = input("Ingresa la marca de tiempo: ")
    publicaciones[nombre_usuario].append({'nombre_usuario': nombre_usuario, 'contenido': contenido, 'marca_tiempo': marca_tiempo})
    print(f"Publicación creada a las {marca_tiempo}.")

while True:
    print("\nRed Social:")
    print("1. Iniciar sesion")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == '1':
        iniciar_sesion()
    elif opcion == '2':
        registrar()
    elif opcion == '3':
        break
    else:
        print("La opcion no es valida, intentalo de nuevo")
