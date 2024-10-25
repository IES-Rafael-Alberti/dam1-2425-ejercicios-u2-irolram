#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

from ej21_04 import pedir_num

def triangulo_letal(num):

    for i in range(1, num):
        print("*" * i)




def main():

    num = pedir_num()
    triangulo_letal(num)

if __name__ == "__main__":
    main()