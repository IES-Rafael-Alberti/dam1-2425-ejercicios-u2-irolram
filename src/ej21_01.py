#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def preguntar_edad():

    edad = int(input("Introduce una edad: "))

    return edad

def mayor_edad(edad)-> bool:

    if edad >= 18:
        return print("Felicidades, eres mayor de edad.")
    else:
        return print("Que pena... aún eres muy pequeño...")

def main():
    edad = preguntar_edad()
    mayor = mayor_edad(edad)
    print(mayor)

if __name__ == "__main__":
    main()