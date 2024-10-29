#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total

def pedir_numero():

    num =int(input("Ingresa un número positivo: "))

    return num

def comprobar_numero(num):

    if num < 0: 
        print("ERROR")
        pedir_numero()

def contar_par_e_impar(num):

    """
    Cuenta los dígitos pares e impares de un número entero positivo.
    
    Args:
        num (int): El número entero positivo a analizar.
    
    Returns:
        Conteo de dígitos pares e impares.
    """

    par = 0
    impar = 0
    while num != 0:
        for i in range(1, num+ 1):
            if i % 2 == 0:
                par = par + 1
            else:
                impar = impar + 1
        num = pedir_numero()
    return par, impar

def main():

    num = pedir_numero()
    comprobar_numero(num)
    par,impar = contar_par_e_impar(num)

    print("Los números tienen los siguientes números pares e impares: \n Par: {} \n Impar: {}".format(par, impar))

if __name__ == "__main__":
    main()