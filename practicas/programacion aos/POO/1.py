class calculadora_calorias:
    def __init__(self):
        self.alimentos = []
        self.calorias = []

    def add_comida(self, comida, calorias):
        self.alimentos.append(comida)
        self.calorias.append(calorias)

    def ver_eat(self):
        for comida in self.alimentos:
            print(comida)

    def sum_cal(self):
        return sum(self.calorias)

mi_cal = calculadora_calorias()
menu = 1
while menu == 1:
    decision = input("SELECCIONE\n"
                     "1. añadir comidas y calorias\n"
                     "2. ver total de calorias\n"
                     "3. ver comidas\n"
                     "4. salir\n"
                     "DIGITE SU ELECCION: ")
    if decision == "1":
        salir = 0
        while salir == 0:
            comida = input("DIGITE EL NOMBRE DE LA COMIDA o 'salir' para finalizar: ")
            if comida.lower()== "salir":
                salir = 1
                break
            calorias = float(input("DIGITE LAS CALORÍAS DE LA COMIDA: "))
            mi_cal.add_comida(comida, calorias)

    elif decision == "2":
        total_calorias = mi_cal.sum_cal()
        print("El total de calorías es:", total_calorias)

    elif decision == "3":
        print("Las comidas registradas son:")
        mi_cal.ver_eat()

    else:
        menu = 2
