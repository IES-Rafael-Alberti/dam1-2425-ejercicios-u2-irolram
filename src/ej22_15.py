#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

def intro_numero():

    num = int(input("Introduce un numero entero: "))

    return num

def comprobar_num(num):
    
    
    cont_num = num
    while num != 0:
        

        num = int(input("Introduce un numero entero: "))
        if num >= 0:
                    cont_num = cont_num + num
 
        else:
            print("ERROR, introduce un número positivo.")
            num = int(input("Introduce un numero entero: "))
           

    return cont_num


def main():

    num = intro_numero()
    suma = comprobar_num(num)

    print("La suma total de los números es: {}".format(suma))


if __name__ == "__main__":
    main()