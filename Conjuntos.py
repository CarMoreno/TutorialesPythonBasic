# Ejemplo de Conjuntos
numeros_pares = { 20, 40, 50, 20, 60, 70, 20, 80, 90, 100, 20 }
numeros_divisibles_cinco = set([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
conjunto_letras = set(['a', 'b', 'c', 'd', 'z', 'e', 'f'])

conjunto_eniver_pino = set(  )
print(conjunto_eniver_pino)

#ocurrencia = 'Z' in conjunto_letras
#print ("Ocurrencia")
#print (ocurrencia)

# UNION ENTRE CONJUNTOS
conjunto_union = numeros_pares | numeros_divisibles_cinco | conjunto_letras
#print (conjunto_union)

# INTERSECCION ENTRE CONJUNTOS
conjunto_interseccion = numeros_pares & numeros_divisibles_cinco
# print(conjunto_interseccion)

# RESTA EXCLUSIVA / O EXCLUSIVO
conjunto_resta_exclusiva = numeros_pares ^ numeros_divisibles_cinco
#print (conjunto_resta_exclusiva)

# RESTA NORMAL
conjunto_resta = numeros_divisibles_cinco - numeros_pares
# print (conjunto_resta)

# VERIFICAR SI UN CONJUNTO ES SUBCONJUNTO DE OTRO:
print ("Conjunto Interseccion")
print (conjunto_interseccion)
respuesta = conjunto_interseccion.issubset(numeros_pares)
respuesta_2 = numeros_pares.issuperset(conjunto_interseccion)
print (respuesta_2)
numeros_pares.add(110)
# numeros_pares.discard(20)

# print (numeros_pares)
# print ("------------------------")
# print (numeros_divisibles_cinco)
# print ("------------------------")
# print (conjunto_vacio)
# for par in numeros_pares:
#     mitad = int( par / 2)
#     print (mitad)

















