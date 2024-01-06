class maquina_de_cambio:
    tasas = {
        "dolares": {
            "pesos colombianos": 4.1,
            "euros": 0.94,
            "pesos argentinos": 0.0029,
            "bolivares": 56.84
        },
        "euros": {
            "pesos colombianos": 4.4,
            "pesos argentinos": 0.0027,
            "bolivares": 60.14,
            "dolares": 0.95
        },
        "pesos argentinos": {
            "pesos colombianos": 12.05,
            "euros": 0.0027,
            "bolivares": 0.16,
            "dolares": 0.0029
        },
        "pesos colombianos": {
            "dolares": 0.00024,
            "euros": 0.00022,
            "pesos argentinos": 0.083,
            "bolivares": 0.013
        },
        "bolivares": {
            "dolares": 0.18,
            "euros": 0.017,
            "pesos argentinos": 6.16,
            "pesos colombianos": 74.13
        }
    }

    def conversion(self, moneda_inicial, dinero, moneda_convertir):
        if moneda_inicial in self.tasas and moneda_convertir in self.tasas[moneda_inicial]:
            conver = self.tasas[moneda_inicial][moneda_convertir] * dinero
            return conver
        else:
            return None

mi_tas = maquina_de_cambio()

bucle_menu = 0
while bucle_menu == 0:
    print("Digite 'salir' cuando desee salir del programa")
    moneda_inicial = input("Escriba el nombre de su moneda inicial: ")
    dinero = input("Digite la cantidad de dinero: ")
    moneda_convertir = input("Escriba el nombre de la moneda a la que desea convertir: ")

    if moneda_inicial.lower() == "salir" or dinero.lower() == "salir" or moneda_convertir.lower() == "salir":
        bucle_menu = 1
    else:
        dinero = float(dinero)
        conversion_result = mi_tas.conversion(moneda_inicial, dinero, moneda_convertir)
        if conversion_result is not None:
            print("El resultado de la conversión es:", conversion_result)
        else:
            print("Las monedas ingresadas no son válidas. Por favor, inténtelo nuevamente.")
