#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

from ej22_15 import intro_numero

def ordenar_lista(num):

    
    while num != 0:
        
        num = int(input("Introduce un numero entero: "))
        lista_num = []

        if num == 0:
            return lista_num
        
            

    return lista_num.sort()

def main():
    num = intro_numero()

    lista = ordenar_lista(num)

    print("El número mayor fue: {}".format(lista))

if __name__ == "__main__":
    main()