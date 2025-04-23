inventario = int(input("Cuantos pares de zapatos tienes en el inventario?: "))
print(f"El inventario contiene {inventario} pares de zapato")
transaccion = 0

while inventario > 0:
    vendidos = int(input("Cuantos pares de zapatos se vendieron?:"))
    inventario -= vendidos
    print(f"Quedan {inventario} pares de zapatos")
    transaccion += 1

if vendidos > inventario:
    print(f"No hay suficientes pares de zapatos en stock. Solo hay, {inventario} pares de zapatos dispomibles")

else:
    inventario -= vendidos
    print(f"Quedan {inventario} pares de zapatos")
    transaccion += 1

print (f"Se han realizado {transaccion} transacciones")
