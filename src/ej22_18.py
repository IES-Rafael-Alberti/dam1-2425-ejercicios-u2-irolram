#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


from ej22_14 import intro_numero


def suma_num(num):
    guardar_num = ""
    contador = 0

    for i in range(1, num + 1):
                
        contador = contador + i
        guardar_num += str(i) + ", "

        if i == num:
            guardar_num = guardar_num.removesuffix(", ")

    return guardar_num, contador


def acabar_programa(suma: int,contador,par):
    
    print("La suma de los digitos son: {}\n El numero es: {}\n Los numeros pares son {}".format(suma, contador, par))


def numeros_pares(num):

    lista_par = ""
    
    if num % 2 == 0:
        lista_par += str(num) + ", "
        return num


def main():

    num = intro_numero()


    suma, contador = suma_num(num)
    par = numeros_pares(num)

    while str(num) != ("-1"):
        intro_numero()
    else: 
        acabar_programa(suma,contador,par)
    



if __name__ == "__main__":
    main()