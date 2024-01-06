class maquina_de_intereses:
    def __init__(self, inversion, tasa, mes, cant_meses):
        self.inversion = inversion
        self.tasa = tasa
        self.mes = mes
        self.cant_meses = cant_meses

    def calculo_mensual(self):
        for i in range(self.cant_meses):
            ganancia_mensual = self.inversion * self.tasa
            self.inversion += ganancia_mensual
            print(f"Mes {self.mes}: Inversión actual: {self.inversion:.2f}")
            self.mes += 1

    def obtener_inversion_final(self):
        return self.inversion

inversion_inicial = float(input("ingrese la cantidad a invertir: "))
tasa_interes = float(input("ingrese la tasa de interes mensual (porcentaje): ")) / 100
cantidad_meses = int(input("ingrese la cantidad de meses: "))

maquina = maquina_de_intereses(inversion_inicial, tasa_interes, 1, cantidad_meses)

print("\nEvolución de la inversión mensual:")
maquina.calculo_mensual()

inversion_final = maquina.obtener_inversion_final()
print(f"\nInversión final después de {cantidad_meses} meses: {inversion_final:.2f}")
