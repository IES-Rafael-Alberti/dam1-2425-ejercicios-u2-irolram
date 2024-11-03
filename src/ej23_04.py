#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

def pedir_num():

    try:
        num = int(input("Dame un número: "))

        if num < 0:
            raise  ValueError("El número debe ser positivo")
        
        
    except ValueError as e:
        print(f"Error {e}")

        return pedir_num()
    
    return num


def main():

    pedir_num()


if __name__ == "__main__":
    main()  
