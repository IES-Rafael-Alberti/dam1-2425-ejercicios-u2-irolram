#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def preguntar_nombre_sexo():

    nom = input("Introduzca su nombre: ")
    sexo = input("Introduzca su sexo M/F: ")


    return nom.upper(), sexo.upper()

def comprobar_nom(nom):
    
    while nom == "":
        nom= input("ERROR, introduce tu nombre: ")
    return nom.upper()

    
def comprobar_sexo(sexo):

    while sexo != "M" and sexo != "F":
        sexo = input("Introduzca su sexo M/F: ")
    return sexo.upper()

def grupos(nom, sexo):
    
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