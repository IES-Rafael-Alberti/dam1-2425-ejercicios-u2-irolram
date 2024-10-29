#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

def pedir_numero():

    num = int(input("Ingrese un número mayor que 0: "))

    return num

def condiciones_num():

    cont_primo = 0
    while True:
        num = pedir_numero()
        if num < 0:
            print("ERROR, solo números positivos")
            num = pedir_numero()
        
        elif num == 0:
            return cont_primo
            
            

        elif comprobar_primo(num):
            cont_primo += 1


def comprobar_primo(num):

    if num < 2:
        return False
    for i in range(2, num):
         if num % i == 0:
            return Falses
    return True


def main():
    primo= condiciones_num()
    print("Fin, la cantidad de números primos son: {}".format(primo))
    
if __name__ == "__main__":
    main()
