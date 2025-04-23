inventario = 100
print (f"El inventario contiene {inventario} hamburguesas")
while inventario > 0:
    if inventario <= 10:
        print("ADVERTENCIA: EL INVENTARIO ESTÁ CASI VACIO.")
    num_hamburguesas = int(input("Cuantas hamburguesas quiere el cliente? "))
    if num_hamburguesas>inventario:
        print(f"No hay suficientes hamburguesas en stock. solo quedan {inventario} hamburguesas ")
    else:
        inventario -= num_hamburguesas
        print(f"El cliente a pedido {num_hamburguesas} hamburguesas. Ahora quedan {inventario} hamburguesas. ")
    if inventario == 0:
        break
print("Sorry bro, ya no hay hamburguesas :(")