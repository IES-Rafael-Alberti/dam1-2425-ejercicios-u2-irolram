#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correc

def pedir_num():

    try:
        num = int(input("Dame un número: "))

        if num < 0:
            raise  ValueError("El número debe ser positivo")
        
        
    except ValueError as e:
        print(f"Error {e}")

        return pedir_num()
    
    return num

def cuenta_atras(num):

    guardar_numeros = ""

    for i in range(num, -1, -1):
        guardar_numeros += str(i) + ", "

        if i == 0:
            guardar_numeros = guardar_numeros.removesuffix(", ")


    return guardar_numeros

def main():

    num =pedir_num()

    atras = cuenta_atras(num)

    print("La cuenta atrás del número que has pedido es: {}".format(atras))

if __name__ == "__main__":
    main()   