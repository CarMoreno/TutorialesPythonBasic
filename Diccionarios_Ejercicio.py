from Diccionarios import usuario_1, usuario_2
paises = [
    {
        "id": 1000,
        "nombre": "Colombia",
        "capital": "Bogotá",
        "idioma": "Español",
        "poblacion": 45000000
    },
    {
        'id': 2000,
        "nombre": "Ecuador",
        "capital": "Quito",
        "idioma": "Español",
        "poblacion": 6500000
    },
    {
        'id': 3000,
        "nombre": "Reino Unido",
        "capital": "Londres",
        "idioma": "Ingles",
        "poblacion": 6500000
    },
    {
        'id': 6000,
        "nombre": "Estados Unidos",
        "capital": "Washington",
        "idioma": "Ingles",
        "poblacion": 4670000
    },
    {
        "id": 4000,
        "nombre": "China",
        "capital": "Pekín",
        "idioma": "Mandarín",
        "poblacion": 8900000000
    },
    {
        "id": 5000,
        "nombre": "Argentina",
        "capital": "Buenos aires",
        "poblacion": 540000
    },
]

lista_paises_idioma_espanol = []
lista_paises_idioma_ingles = []
lista_paises_otros_idiomas = []

# CLASIFICACION DE IDIOMAS
for pais in paises:
    idioma = pais.get("idioma", False)
    nombre = pais.get("nombre", False)
    if idioma == False:
        print("No existe el idioma en el diccionario para el pais " + nombre)
    else:
        # CONVERTIMOS EL STRING EN MAYUSCULA Y QUITAMOS ESPACIOS
        if (idioma.upper().replace(" ", "") == "ESPAÑOL"):
            lista_paises_idioma_espanol.append(pais)
        elif (idioma.upper().replace(" ", "") == "INGLES"):
            lista_paises_idioma_ingles.append(pais)
        else:
            lista_paises_otros_idiomas.append(pais)

def mostrar_listas():
    print(lista_paises_idioma_espanol)
    print(lista_paises_idioma_ingles)
    print(lista_paises_otros_idiomas)


print (usuario_2)
