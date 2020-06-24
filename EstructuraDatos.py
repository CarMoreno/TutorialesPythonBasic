lista_nombres = ['Eniver', 'Carlos']
lista_edades = [32, 25]
#                      0                  1
lista_informacion = [lista_nombres, lista_edades]
lista_informacion_actualizada = []
# print(lista_informacion)

# for nombre in lista_nombres:
#     nombre = nombre.lower() + ' Pino'
#     print(nombre)
# tamano_lista = len(lista_nombres)
# #             [0, 1]
# for indice in range(tamano_lista):
#     nombre = lista_nombres[indice]
#     print(nombre)
# #                [0, 1]
for indice in range(len(lista_informacion)):
    if indice == 0:
                       # CLONAMOS LISTA_NOMBRE
        lista_nombre = list(lista_informacion[indice])
        nombre_con_apellidos = ''
                    # [ 0, 1 ]
        for indice in range(len(lista_nombre)):
            nombre_con_apellidos = lista_nombre[indice] + ' Pino'
            lista_nombre[indice] = nombre_con_apellidos.upper()
            # lista_nombre[0] = 'Eniver' + ' Pino'
            # lista_nombre[1] = 'Carlos' + ' Pino'
        print(lista_nombre)
    else:
        # Indice = 1
        #            CLONAMOS LISTA_EDADES
        lista_edad = list(lista_informacion[indice])
        edad_por_dos = 0
        #             [    0,   1 ]
        for indice in range(len(lista_edad)):
            edad_por_dos = lista_edad[indice] * 2
            lista_edad[indice] = edad_por_dos
        print(lista_edad)


print(lista_informacion)





# lista_numeros = range(10) # [0,1,2,3,....9]


