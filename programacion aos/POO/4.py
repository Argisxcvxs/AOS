class agenda:
    def __init__(self, asignatura, tarea, fecha_entrega, prioridad):
        self.asignatura = asignatura
        self.tarea = tarea
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad

    def agregar_proyecto(self, asignatura, tarea, fecha_entrega, prioridad):
        if asignatura in proyectos:
            proyectos[asignatura].append({"tarea": tarea, "fecha_entrega": fecha_entrega, "prioridad": prioridad})
        else:
            proyectos[asignatura] = [{"tarea": tarea, "fecha_entrega": fecha_entrega, "prioridad": prioridad}]

    def visualizar(self):
        for asignatura, tareas in proyectos.items():
            print(f"Asignatura: {asignatura}")
            for tarea in tareas:
                print(f"Tarea: {tarea['tarea']}")
                print(f"Fecha de entrega: {tarea['fecha_entrega']}")
                print(f"Prioridad: {tarea['prioridad']}")
                print()

agend = agenda("", "", "", "")  # Inicialización de la clase sin ningun parametro
proyectos = {}

agregar_proyectos = 0

while agregar_proyectos != 3:
    dia = input("Ingrese el día de estudio: ")
    if dia == "1" or dia == "2":
        print(f"Día {dia} de estudio")
        print("-------------------")
        asignatura = input("Ingrese el nombre de la asignatura: ")
        tarea = input("Ingrese el nombre de la tarea: ")
        fecha_entrega = input("Ingrese la fecha de entrega (dd/mm/aaaa): ")
        prioridad = input("Ingrese la prioridad (alta, media, baja): ")

        agend.agregar_proyecto(asignatura, tarea, fecha_entrega, prioridad)

        if dia == "2":
            print("\nProyectos de Estudio")
            print("--------------------")
            agend.visualizar()
    else:
        agregar_proyectos = 3
