#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def num_positivo():

    num = int(input("Introduce un número positivo: "))

    return num

def comprobar_posi(num):

    while num < 0:
        num = int(input("DAME UN NÚMERO POSITIVO: "))
    return num

def numeros_impares(num): 

    guardar_num = ""

    if num % 2 == 0:

        num = num - 1

        for i in range(1, num + 1, 2 ):
            guardar_num += str(i) + ", "
            if i == num:
                guardar_num = guardar_num.removesuffix(", ")
        print("Los números impares son: {}".format(guardar_num))
    else:

        for i in range(1, num + 1, 2):
            guardar_num += str(i) + ", "
            if i == num:
                guardar_num = guardar_num.removesuffix(", ")
        print("Los números impares son: {}".format(guardar_num))

def main():

    num = num_positivo()
    comprobar_posi(num)

    numeros_impares(num)


if __name__ == "__main__":
    main() 