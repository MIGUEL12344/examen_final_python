"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
#metodo de compresion en la funcion def
def filtrar_numeros_primos(lista_numeros):
#Función que filtra los números primos de una lista
    return list(filter(lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)), lista_numeros))

# mostrar por consola
primos_filtrados = filtrar_numeros_primos([4, 7, 10, 4, 1, 0, 13, 17, 23])
print("Números primos:", primos_filtrados)  