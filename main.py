Inventario = {
    "Huevos": 12000,
    "Leche": 5000, 
    "Pan": 4000,
    "Pasta": 2500,
    "Lentejas": 2700, 
    "Arroz": 3000, 
    "Carne": 8000, 
    "Alverja": 3500
}
Promociones = {
    "Alverja": 0.10,
    "Huevos": 0.20,
    "Pan": 0.5
}

def mostrar_inventario():
    print ("---------Inventario---------")
    for producto, precio in Inventario.items():
        print(f"{producto}: ${precio}")

def aplicar_promociones():
    print("\n------Promocion------")

    for producto, descuento in Promociones.items():
        precio = Inventario[producto] 
        precio_final = precio - (precio * descuento)

        print(f"{producto}: ${precio_final}")

mostrar_inventario()
aplicar_promociones()