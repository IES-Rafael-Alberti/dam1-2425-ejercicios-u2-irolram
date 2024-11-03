#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

def pedir_numeros():
    """
    Solicita al usuario dos números enteros

    Returns:
        tuple: Un par de enteros ingresados por el usuario
    """

    num1 = int(input("Dame un número: "))
    num2 = int(input("Dame otro número: "))


    return num1, num2

def comprobar_num2(num2):

    """
    Verifica que el segundo número no sea cero. Si es cero, solicita otro número hasta que sea distinto de cero.

    Args:
        num2 (int): El número a verificar.

    Returns:
        int: Un número distinto de cero.
    """

    while num2 == 0:
        num2 = int(input("ERROR, Dame otro número: "))
    return num2
    
def division_de_numeros(num1, num2):
    
    division = (num1 / num2)

    return division

def main():
    num1, num2 = pedir_numeros()
    comprobar_num2(num2)
    division = division_de_numeros(num1, num2)
    print("La división de los números {}, {} es: {}".format(num1, num2, division))

if __name__ == "__main__":
    main()