#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def preguntar_nombre_sexo():
    """
    Solicita al usuario que introduzca su nombre y sexo.
    
    Returns:
        tuple: Una tupla con el nombre en mayúsculas y el sexo en mayúsculas.
    """

    nom = input("Introduzca su nombre: ")
    sexo = input("Introduzca su sexo M/F: ")


    return nom.upper(), sexo.upper()

def comprobar_nom(nom):
    """
    Verifica que el nombre no esté vacío, en caso contrario, lo solicita de nuevo.

    Args:
        nom (str): El nombre ingresado por el usuario.
    
    Returns:
        str: El nombre validado en mayúsculas.
    """
    
    while nom == "":
        nom= input("ERROR, introduce tu nombre: ")
    return nom.upper()

    
def comprobar_sexo(sexo):
    """
    Verifica que el sexo sea 'M' o 'F', en caso contrario, lo solicita de nuevo.

    Args:
        sexo (str): El sexo ingresado por el usuario.
    
    Returns:
        str: El sexo validado en mayúsculas.
    """
    
    while sexo != "M" and sexo != "F":
        sexo = input("Introduzca su sexo M/F: ")
    return sexo.upper()

def grupos(nom, sexo):
    """
    Determina y muestra el grupo correspondiente basado en el nombre y el sexo.

    Args:
        nom (str): El nombre validado del usuario.
        sexo (str): El sexo validado del usuario.
    """

    if sexo == "F" and nom < "M":
        print("Grupo A")
    elif sexo == "M" and nom > "N":
        print("Grupo A")
    else: 
        print("Grupo B")

def main():
    nom, sexo = preguntar_nombre_sexo()
    comprobar_sexo(sexo)
    comprobar_nom(nom)
    grupos(nom, sexo)

if __name__ == "__main__":
    main()