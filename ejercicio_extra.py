"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
# Diccionario de tiendas comerciales
tiendas = {
    1: {'nombre': 'negocio elver 1', 'horario': '9:00 - 18:00'},
    2: {'nombre': 'negocio galarga 2', 'horario': '10:00 - 19:00'},
    3: {'nombre': 'negocio paco 3', 'horario': '8:30 - 17:30'},
    4: {'nombre': 'negocio merte 4', 'horario': '11:00 - 20:00'},
    5: {'nombre': 'negocio gonzales 5', 'horario': '9:30 - 18:30'}
}

# Función para imprimir las tiendas comerciales
def imprimir_tiendas(tiendas):
    print("Tiendas comerciales:")
    for clave, valor in tiendas.items():
        print(f"{clave}: {valor['nombre']} - Horario: {valor['horario']}")

# Función para editar el nombre de una tienda comercial
def editar_nombre_tienda(tiendas, id_tienda, nuevo_nombre):
    if id_tienda in tiendas:
        tiendas[id_tienda]['nombre'] = nuevo_nombre
        print(f"Nombre de la tienda actualizado correctamente.")
    else:
        print(f"No existe una tienda con el ID {id_tienda}.")

# Función para actualizar el horario de atención de una tienda comercial
def actualizar_horario(tiendas, id_tienda, nuevo_horario):
    if id_tienda in tiendas:
        tiendas[id_tienda]['horario'] = nuevo_horario
        print(f"Horario de la tienda actualizado correctamente.")
    else:
        print(f"No existe una tienda con el ID {id_tienda}.")

# Función para eliminar una tienda comercial
def eliminar_tienda(tiendas, id_tienda):
    if id_tienda in tiendas:
        del tiendas[id_tienda]
        print(f"Tienda eliminada correctamente.")
    else:
        print(f"No existe una tienda con el ID {id_tienda}.")

# mostrar por consola
imprimir_tiendas(tiendas)

print("\n--- tiendas editadas ---")
editar_nombre_tienda(tiendas, 3, 'negocio ohhh babosa')
imprimir_tiendas(tiendas)

print("\n--- actualizar tiendas ---")
actualizar_horario(tiendas, 2, '10:30 - 19:30')
imprimir_tiendas(tiendas)

print("\n--- Eliminar tienda ---")
eliminar_tienda(tiendas, 4)
imprimir_tiendas(tiendas)

