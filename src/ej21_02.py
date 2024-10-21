#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def contrasena_comprobar():

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