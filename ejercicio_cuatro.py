"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me "permita editar uno de los campos del registro
"""
# Diccionario con dos registros de un alumno
alumno = {
    'nombre': 'Juan Pérez',
    'edad': 20,
    'curso': 'Python avanzado',
    'promedio': 15
}

# Función para imprimir los registros del alumno
def imprimir_registro(alumno):
    print("Registro del alumno:")
    for clave, valor in alumno.items():
        print(f"{clave}: {valor}")

# Función para editar la edad del alumno
def editar_edad(alumno, nueva_edad):
    alumno['edad'] = nueva_edad

# mostrar resultado del primer resultado por consola
print("primer registro")
imprimir_registro(alumno)
# mostrar resultado del segundo resultado por consola
print("\nsegundo registro")
nueva_edad = 22
editar_edad(alumno, nueva_edad)
imprimir_registro(alumno)

