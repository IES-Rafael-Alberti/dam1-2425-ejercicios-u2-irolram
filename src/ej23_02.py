#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def pedir_num():

    try:
        num = int(input("Dame un número: "))

        if num < 0:
            raise  ValueError("El número debe ser positivo")
        
        
    except ValueError as e:
        print(f"Error {e}")

        return pedir_num()
    
    return num
    
def numeros_impares(num):

    guardar_num = " "
    if num % 2 == 0:
        for i in range(1, num +1, 2):
            guardar_num += str(i) + ", "

            if i == num -1:
                guardar_num = guardar_num.removesuffix(", ")
    else: 
        for i in range(1, num +1, 2):
            guardar_num += str(i) + ", "

            if i == num:
                guardar_num = guardar_num.removesuffix(", ")

    return guardar_num

def main():

    num = pedir_num()

    impar = numeros_impares(num)

    print("Los numeros impares del número recibido son: {}".format(impar) )
    
if __name__ == "__main__":
    main()