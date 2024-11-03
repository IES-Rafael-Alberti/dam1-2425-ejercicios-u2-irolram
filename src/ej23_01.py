#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def pedir_edad() ->int:

    edad_incorrecta = True

    while edad_incorrecta:

        try:
            edad  = None
            edad = int(input("Introduce tu edad: "))

            if edad < 0:
                raise ValueError("La edad debe ser positiva")
            if edad == 0:
                raise ValueError("Tu ere mu chico pa escribir en un ordenador")
            if edad > 125:
                raise ValueError("No existe momia tan vieja")
            
            edad_incorrecta = False
        except ValueError as e: 
            if edad is None:

                print(f"ERROR {e}. Intentalo de nuevo")
            else:
                print(f"ERROR {e}. Intentalo de nuevo")
    
    return edad

def mostrar_anios_cumplidos(edad: int):

    for i in range(1, edad + 1):
        if i == edad:
            print(i)
        else:
            print(i, end=", ")

def main():
    edad = pedir_edad()
    print(f"Has cumplido los siguientes años: ")
    mostrar_anios_cumplidos(edad)


if __name__ == "__main__":
    main()