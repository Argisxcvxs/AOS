#2
def fibonacci(n): #se define la funcion con el n que representa el numero de elementos en la serie
    if n <= 0: #si es menor o igual a 0 la serie no cuenta asi que sale vacia
        return []
    elif n == 1: #si es 1 la la lista sera 0 porque no hay multiplos que den otro valor
        return [0]
    elif n == 2: # si es 2 dara 0 y luego 1, estos son los primeros elementos de la serie
        return [0, 1]
    else: #Se utiliza un bucle while para calcular los términos de la serie de Fibonacci. El bucle se ejecuta mientras la longitud de la lista fibsea menor que n En cada iteración y se agrega a la lista fib la suma de los dos últimos elementos de la lista
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

n = int(input("Ingrese el número de elementos de la serie de Fibonacci que desea calcular: ")) #usamos la variable n para depositar los datos de hasta donde llegara la serie
resultado = fibonacci(n) #se define el resultado de la serie en una sola variable para imprimirla
print("La serie de Fibonacci es:", resultado)