#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def intro_palabra():

    palabra= input("Introduce una palabra: ")

    return palabra

def palabra_a_palabra(palabra):

    

    for i in range(len(palabra)):
        print(palabra [i])


def main():

    palabra = intro_palabra()

    palabra_a_palabra(palabra)

if __name__ == "__main__":
    main()