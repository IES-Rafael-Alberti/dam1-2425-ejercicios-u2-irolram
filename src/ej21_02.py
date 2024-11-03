#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def contrasena_comprobar():
    """
    Solicita al usuario que ingrese una contraseña y la compara con una contraseña almacenada.

    La función obtiene la contraseña ingresada, la convierte a minúsculas y la compara con la contraseña guardada.
    Si coinciden, se indica que la contraseña es correcta; de lo contrario, se indica que es inválida.

    Returns:
        str: Mensaje indicando si la contraseña es correcta o incorrecta.
    """
        

    contraguardada = "contraseña"
    contra = input("Escribe la contraseña: ")

    if contra.lower() == contraguardada:
        return "Contraseña correcta, accediendo a tus datos del banco."
    else:
        return "Contraseña invalida"

def main():

    contra = contrasena_comprobar()
    print(contra)


if __name__ == "__main__":
    main()