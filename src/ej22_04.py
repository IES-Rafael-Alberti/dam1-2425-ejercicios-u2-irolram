#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

from ej22_03 import num_positivo

def cuenta_atras(num):
    
    primer_numero = num
    atras = ""
    while num  > 0:
        num = num - 1
        
        if num > 0:
            atras += str(num) + ", "
        else:
            atras += str(num) + " "
    
    print("Toma los números desde el número {}: {}".format(primer_numero, atras))

def main():

    num = num_positivo()

    cuenta_atras(num)


if __name__ == "__main__":
    main()  