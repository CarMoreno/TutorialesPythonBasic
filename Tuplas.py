fecha_cumple_carlos = (20, 'Junio', 1995)
fecha_cumple_eniver = tuple([29, 'Mayo', 1988])
tuplas_unico = tuple([1])
tuplas_unico_2 = (3,)
tipo = type(tuplas_unico_2) #AVERIGUAR EL TIPO DE CUALQUIER VARIABLE
#print (tipo)
#tupla[1] = 'Diciembre'

# RECORRER TUPLAS:
#             [ 0, 1, 2 ]
for indice in range(len(fecha_cumple_carlos)):
    print(fecha_cumple_carlos[indice])

print ("==============================================")

for item in fecha_cumple_eniver:
    print(item)
