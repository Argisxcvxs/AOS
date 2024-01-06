persona = {"juan": 1000}

class cajero:
    def __init__(self, dinero, usuario):
        self.dinero = dinero
        self.usuario = usuario
    
    def retirar(self, retiro):
        if self.dinero > retiro:
            self.dinero -= retiro
            return retiro
        else: 
            return "Error, vuelva a intentarlo"
    
    def consignar(self, dinero_consignado):
        self.dinero += dinero_consignado
        return dinero_consignado

mi_cajero = cajero(persona["juan"], "juan")

menu = 1
while menu == 1:
    decision = input("SELECCIONE \n\
                     1. DEPOSITAR DINERO \n\
                     2. RETIRAR DINERO \n\
                     3. CONSULTAR SU SALDO \n\
                     4. SALIR DEL PROGRAMA \n\
                     DIGITE SU ELECCION: ")
    
    if decision == "1":
        dinero_consignado = float(input("DIGITE LA CANTIDAD DE DINERO QUE DESEA DEPOSITAR: "))
        print(mi_cajero.consignar(dinero_consignado))
        
    elif decision == "2":
        retiro = float(input("DIGITE LA CANTIDAD DE DINERO QUE DESEA RETIRAR: "))
        print(mi_cajero.retirar(retiro))
        
    elif decision == "3":
        print(mi_cajero.dinero)
        
    else: 
        menu = 2
