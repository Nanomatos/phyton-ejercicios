#Declarar Variables
#nombre = input("¿Cual es tu nombre? ")
edad = int(input("¿Cual es tu edad? "))
#print(f"Hola {nombre} tienes {edad} años!")

#def saludar(nombre):
    #print (f"Hola {nombre} Bienvenid@ al taller!")
#saludar(nombre)

#Bucle for y while
#for recorrer in range(1,11):
    #print(recorrer)

def esMayorDeEdad(edad):
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres Menor de edad"
print(esMayorDeEdad(edad))