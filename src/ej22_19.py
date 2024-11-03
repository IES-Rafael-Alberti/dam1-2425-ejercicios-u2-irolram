#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

def intro_opciones():
    """
    Solicita al usuario que ingrese una opción del menú y devuelve la opción seleccionada como un número entero.
    
    Return:
        int: La opción ingresada por el usuario (1, 2 o 3)."""
     

    num = int(input("Ingrese 1- comenzar programa, 2- imprimir listado, 3-finalizar programa: "))

    return num 

def lo_que_pasa_con_opciones():

    """
    Controla el programa de la siguiente manera
    
    - Opción 1: Muestra un mensaje indicando que el programa ha comenzado.
    - Opción 2: Muestra un mensaje que representa un listado.
    - Opción 3: Finaliza el programa y termina el bucle.
    - Cualquier otro número: Muestra un mensaje de error y permite al usuario intentar de nuevo.
    """


    num = intro_opciones()

    while num < 4 and num > 0:

        if num == 1:
            print("El programa ha comenzado")
            
        elif num == 2:
            print("Aquí está el listado")
            
        elif num == 3:
            print("Programa finalizado")
            break
        
        else:
            print("ERROR")
        num = intro_opciones()

def main():

    lo_que_pasa_con_opciones()

if __name__ == "__main__":
    main()