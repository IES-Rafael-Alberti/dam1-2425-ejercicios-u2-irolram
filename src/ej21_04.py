#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def pedir_num():

    num = int(input("Dame un numero: "))

    return num

def comprobar_par(num):
    if num % 2 == 0:
        return print("El número es par")
    else:
        return print("El número es impar")

def main():
    num = pedir_num()
    comprobar_par(num)


if __name__ == "__main__":
    main()