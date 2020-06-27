def mi_function():
    print("Hola Mundo")

#variable_guardar = mi_function

#variable_guardar()
#nombre, apellido, edad, genero, tipo_sangre, estatura
def es_mayor_edad(edad):
    if edad >= 18:
        return True
    return False

def es_adolescente(edad):
    if edad >= 13 and edad <= 17:
        return True
    return False

def dar_informacion(**datos_usuario):
    edad = datos_usuario.get('edad', 18)
    if es_mayor_edad(edad):
        return f"""| --- CEDULA DE CIUDADANIA ---
    |* Nombre de usuario: {datos_usuario['nombre']} |
    |* Apellido: {datos_usuario['apellido']} |
    |* Edad: {datos_usuario.get('edad', 18)} |
      """
    elif es_adolescente(edad):
        return f"""| --- TARJETA DE IDENTIDAD ---
    |* Nombre de usuario: {datos_usuario['nombre']} |
    |* Apellido: {datos_usuario['apellido']} |
    |* Edad: {datos_usuario.get('edad', 18)} |
    """
    else:
        return f"""| --- REGISTRO CIVIL ---
    |* Nombre de usuario: {datos_usuario['nombre']} |
    |* Apellido: {datos_usuario['apellido']} |
    |* Edad: {datos_usuario.get('edad', 18)} |
    """

def mostrar_datos(**datos_usuario):
    informacion = dar_informacion(**datos_usuario)
    print(informacion)


mostrar_datos(nombre='Eniver', apellido='Pino', edad=4, RH='o+')

