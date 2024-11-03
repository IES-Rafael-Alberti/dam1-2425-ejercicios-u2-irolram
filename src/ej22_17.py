#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


from ej22_15 import intro_numero

def suma_num(num):
    guardar_num = ""
    contador = 0

    for i in range(1, num + 1):

        contador = contador + i
        guardar_num += str(i) + " + "
        if i == num:
            guardar_num = guardar_num.removesuffix("+ ")
        
    print("{} => {} = {}".format(num, guardar_num, contador))

    return contador

def main():

    num = intro_numero()
    suma_num(num)




if __name__ == "__main__":
    main()