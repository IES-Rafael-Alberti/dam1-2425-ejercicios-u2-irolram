#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def pedir_palabra()->str:

    pal = input("Introduce una palabra: ")

    return pal

def repetir_10_veces(pal):

    for _ in range(1,11):
        print(pal)

def main():

    palabra = pedir_palabra()

    repetir_10_veces(palabra)

if __name__ == "__main__":
    main()    