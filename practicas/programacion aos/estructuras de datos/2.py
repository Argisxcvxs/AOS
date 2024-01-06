def contar_elementos(lista):
    diccionario = {}
    for elemento in lista:
        if elemento in diccionario:
            diccionario[elemento] += 1
        else:
            diccionario[elemento] = 1
    return diccionario

# Ejemplo de uso
lista = [1, 2, 3, 2, 1, 3, 3, 4, 5, 4, 4]
resultado = contar_elementos(lista)
print(resultado)
