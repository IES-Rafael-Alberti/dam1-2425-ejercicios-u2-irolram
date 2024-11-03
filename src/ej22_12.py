#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def preguntar_frase():

    frase = str(input("Escribe una frase: "))
    letra = input("Introduce una letra la cual buscar: ")

    return frase, letra

def contar_letra_especifica(frase,letra):
    contador = 0
    for caractere in frase:
        
        if caractere == letra:
            contador = contador + 1

    return contador

def main():

    frase, letra = preguntar_frase()

    contador = contar_letra_especifica(frase, letra)

    print("La frase tenia {} de veces la letra {}".format(contador, letra))

if __name__ == "__main__":
    main()
    