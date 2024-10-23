#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

def pedir_numeros():


    num1 = int(input("Dame un número: "))
    num2 = int(input("Dame otro número: "))


    return num1, num2

def comprobar_num2(num2):

    while num2 == 0:
        num2 = int(input("ERROR, Dame otro número: "))
    return num2
    
def division_de_numeros(num1, num2):
    
    division = int(num1 / num2)

    return division

def main():
    num1, num2 = pedir_numeros()
    comprobar_num2(num2)
    division = division_de_numeros(num1, num2)
    print("La división de los números {}, {} es: {}".format(num1, num2, division))

if __name__ == "__main__":
    main()