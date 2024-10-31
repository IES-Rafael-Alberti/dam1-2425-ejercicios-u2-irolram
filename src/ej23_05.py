#Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!

def pedir_contra():

    try:
        contra = input("Introduzca la contraseña: ")

        if contra != "contraseña":
            raise ValueError("Incorrect Passwored!!")
        else:
            print("Contraseña correcta!!")

    except ValueError as e:
        print("Error, {}".format(e))

    return contra


def main():
    pedir_contra()

if __name__ == "__main__":
    main() 