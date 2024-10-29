#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def introducir_cosos():

    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")

    return frase, letra

def recorrer_frase(frase, letra):

    posicion = 0
    for caractere in frase:
        if caractere == letra:
            print("Se ha encontrado coincidencia en la posición {}".format(posicion))
        else:
            print("No se ha encontrado coincidencias en la posición {}".format(posicion))
        posicion += 1

    print("Ejecución finalizada.")


def main():
    frase,letra = introducir_cosos()

    recorrer_frase(frase, letra)



if __name__ == "__main__":
    main()