#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

"""
Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
"""

def introducir_libro():

    libro = input("Libro: ")

    return libro

def condiciones_de_libro(libro):

    contador_linea = 0
    
    contador_numeros = 0

    for letra in libro:

        if letra in "0123456789":
            contador_numeros = contador_numeros + 1


    while libro != "/" and libro != "*":

        contador_linea = contador_linea + 1
        libro = introducir_libro()
        
    
    if libro == "/":

        print("Línea completa. Aparecen {} dígitos númericos".format(contador_numeros))

    elif libro == "*":

        print("Fin. Se leyeron {} líneas completas".format(contador_linea))
    
    

def main():

    libro = introducir_libro()

    condiciones_de_libro(libro)


if __name__ == "__main__":
    main()