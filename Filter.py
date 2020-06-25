inventario_productos = (
    ['Computador Portatil', 'HP', 2500000, 'Windows 10'],
    ['Mouse', 'Genius', 40000, None],
    ['Smartphone', 'Xiaomi Note 9S', 1000000, 'Android 10'],
    ['Smartphone', 'Xiaomi Note 8S', 800000, 'Android 10'],
    ['Audifonos', 'Apple', 120000, None]
)

def calcular_precio_sin_IVA(registro_producto):
    precio = registro_producto[2]
    nuevo_precio = round(precio / 1.19, 2)
    registro_producto[2] = nuevo_precio
    return registro_producto

def filtrar_productos_smartphone(registro_producto):
    tipo_producto = registro_producto[0]
    if tipo_producto == 'Smartphone':
        return True
    return False

inventario_productos_sin_iva = tuple(map(calcular_precio_sin_IVA, inventario_productos))

smartphones = tuple(filter(filtrar_productos_smartphone, inventario_productos))

#print (smartphones)





lista = [2,3,4,5]

def multiplicar_por_10(numero):
    multiplicacion =  numero * 10
    return multiplicacion

def filtrar_numeros_pares(numero):
    if numero % 2 == 0:
        return True
    return False

lista_numeros_10 = list(map(multiplicar_por_10, lista))
lista_pares = list(filter(filtrar_numeros_pares, lista))
print(lista_numeros_10)










