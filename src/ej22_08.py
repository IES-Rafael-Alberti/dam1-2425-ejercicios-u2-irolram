#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

from ej21_04 import pedir_num

def triangulo_numeros(num):

    for i in range(1, num + 1):

        for j in range(1,i +1):
            print(j, end=' ')  
        print()
    

    

def main():

    num = pedir_num()

    triangulo_numeros(num)

if __name__ == "__main__":
    main()   