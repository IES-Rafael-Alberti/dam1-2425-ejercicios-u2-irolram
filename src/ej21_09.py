#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def edad_cliente():

    edad = int(input("Introduzca su edad: "))

    return edad

def precio_entrada(edad):
    """
    Calcula el precio de entrada en función de la edad.

    Args:
        edad (int): Edad del usuario.

    Returns:
        str: Mensaje con el precio de entrada.
    """
    if edad < 4:
        return print("Su entrada es gratis!!")
    elif edad > 4 and edad < 18:
        return print("Su entrada son 5€")
    elif edad > 18:
        return print("Su entrada son 10€")
    
def main():

    edad = edad_cliente()
    precio_entrada(edad)


if __name__ == "__main__":
    main()