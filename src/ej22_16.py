#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

from ej22_15 import intro_numero

def numero_mayor(num):

    lista_num = 0
    
    while num != 0:

        if num < lista_num: 

            num = int(input("Introduce un numero entero: ")) 
        
        if num > lista_num:
                lista_num = num
                num = int(input("Introduce un numero entero: "))

        if num == 0:
            return lista_num
        
        
                
        
            

    return lista_num.sort()

def main():
    num = intro_numero()

    lista = numero_mayor(num)

    print("El número mayor fue: {}".format(lista))

if __name__ == "__main__":
    main()