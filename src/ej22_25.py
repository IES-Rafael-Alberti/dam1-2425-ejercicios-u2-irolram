#Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def intro_frase():

    frase = input("Introduce frase: ")

    return frase

def almacenar_palabras(frase: str):

    lista_palabras = frase.split()

    palabra_mas_larga = ""


    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    print("La palabra más larga es: {}".format(palabra_mas_larga))

def main():

    frase = intro_frase()

    almacenar_palabras(frase)
    
if __name__ == "__main__":
    main()