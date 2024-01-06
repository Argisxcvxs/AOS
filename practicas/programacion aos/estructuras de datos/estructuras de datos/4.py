def suma_valores(diccionario):
    suma = 0
    for valor in diccionario.values():
        suma += valor
    return suma

mi_diccionario = {"a": 10, "b": 20, "c": 30}

resultado = suma_valores(mi_diccionario)
print(resultado)  
