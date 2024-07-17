"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""
def datos_personales(nombre, apellido, edad, programa_estudio, semestre):
#Función que retorna un diccionario con los datos personales de un alumno
    return {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'programa_estudio': programa_estudio,
        'semestre': semestre
    }
# mostrar por consola
resultado = datos_personales("paco", "gerte", "25", "APSTI", "III")
print(resultado) 