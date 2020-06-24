ciudad_1 = dict({
    "nombre": "Cali",
    "numero_habitantes": 4000000,
    "depto": "Valle"
})

ciudad_2 = dict({
    "nombre": "Tulua",
    "numero_habitantes": 200000,
    "depto": "Valle"
})

usuario_1 = {
    "cedula" : 1116267837,
    "nombre" : "Carlos Andres",
    "apellidos": "Moreno Velez",
    "edad": 25,
    "profesion": "Ingeniera de Sistemas",
    "estatura" : 1.78,
    "ciudad_origen": ciudad_2
}

usuario_2 = {
    "cedula" : 14453556,
    "nombre" : "Eniver",
    "apellidos": "Pino",
    "edad": 32,
    "profesion": "Web Master",
    "estatura" : 1.73,
    "ciudad_origen": ciudad_1
}

# print(usuario_1["estatura"])
# print(usuario_1["nombre"])
# print(usuario_1["ciudad_origen"])
# print (usuario_1.get("comida_favorita", "NO EXISTE ESTA CLAVE"))

# respuesta = "nombre" in usuario_1

# print (respuesta)
# for clave in usuario_1:
#     print ("Clave: " + clave + " -- Valor: " + str(usuario_1[clave]))


#print (usuario_1)
#print (usuario_2)

lista_usuarios = [usuario_1, usuario_2]

for usuario in lista_usuarios:

    cedula = usuario.get("cedula")
    if ( cedula == 1116267837 ):
        usuario["ciudad_actual"] = ciudad_1
    elif ( cedula == 14453556 ):
        usuario["ciudad_actual"] = ciudad_2
    else:
        print("USUARIO NO ENCONTRADO")


# for clave in usuario_1.keys():
#     print (usuario_1[clave])

# usuario_1.clear()
usuario_1.update({
    "apellidos": "MORENO VELEZ",
    "edad": 26,
    "comida_favorita": "Arroz con pollo"
})


#print (usuario_1)
# usuario1_copia = usuario_1.copy()
# usuario1_copia.clear()
# print (usuario1_copia)

print(usuario_1)
#print (lista_usuarios)