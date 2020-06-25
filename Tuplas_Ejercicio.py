inventario_productos = (
    ['Computador Portatil', 'HP', 2500000, 'Windows 10'],
    ['Mouse', 'Genius', 40000, None],
    ['Smartphone', 'Xiaomi Note 9S', 1000000, 'Android 10'],
    ['Audifonos', 'Apple', 120000, None]
)
lista_compradores = [
    ('1116267865', 'Carlos Moreno', 20000),
    ('1123445678', 'Eniver', 100000),
    ('3345678654', 'Juan', 350000)
]

# Precio menos el IVA
for producto in inventario_productos:
    precio_producto = producto[2]
    nuevo_precio = round(precio_producto / 1.19, 3)
    producto[2] = nuevo_precio


for comprador in lista_compradores:
    if comprador[0] == '1116267865':
        lista_compradores.append( ('BONO', 10000, comprador) )

print (lista_compradores)