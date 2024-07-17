"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
#crear una funcion
def encontrar_menor_y_mayor(lista_numeros):
    if len(lista_numeros) == 0:
        return {} 
    menor = lista_numeros[0]
    mayor = lista_numeros[0]
    for num in lista_numeros:
        if num < menor:
            menor = num
        if num > mayor:
            mayor = num
    resultado = {
        'menor': menor,
        'mayor': mayor
    }
    return resultado
# mostrar resultado
resultado = encontrar_menor_y_mayor([4, 7, 10, 4, 1, 0])
print(resultado)

