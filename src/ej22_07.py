#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

from ej21_04 import pedir_num

def tabla_multiplicar(num):
    cont = 0
    for i in range(0, 10 + 1):
        print("{} * {} = {} ".format(num, cont, num * i))
        cont = cont + 1
def main():
    num = pedir_num()

    tabla_multiplicar(num)

if __name__ == "__main__":
    main()