#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def pedir_contra():

    contra = input("Dime la contraseña: ")

    return contra.lower()

def comprobar_contra(contra):   

    contraseña = "contraseña"
    while contra != contraseña:
        contra = input("contraseña incorrecta, introduzca de nuevo la CONTRASEÑA: ")
        contra = contra.lower()
    print("CONTRASEÑA CORRECTA!")

def main():

    contra = pedir_contra()

    comprobar_contra(contra)

if __name__ == "__main__":
    main()