#funcion para ordenar
def ordenar_lista_cadenas(lista):
    lista_ordenada = sorted(lista, key=len)
    return lista_ordenada

#uso
cadenas = ["Hola", "Python", "es", "chevere", "programar"]
lista_ordenada = ordenar_lista_cadenas(cadenas)
print(lista_ordenada)
