# Crear el diccionario de estudiantes
estudiantes = [
    {
        "nombre": "Juan",
        "edad": 18,
        "calificaciones": [85, 90, 92],
        "curso": "Matemáticas"
    },
    {
        "nombre": "María",
        "edad": 17,
        "calificaciones": [80, 88, 95],
        "curso": "Historia"
    },
    {
        "nombre": "Carlos",
        "edad": 16,
        "calificaciones": [95, 92, 88],
        "curso": "Ciencias"
    }
]

# Mostrar la información de los estudiantes
for estudiante in estudiantes:
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Calificaciones:", estudiante["calificaciones"])
    print("Curso:", estudiante["curso"])
    print("--------------------")
