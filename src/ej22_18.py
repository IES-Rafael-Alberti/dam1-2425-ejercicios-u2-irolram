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

def acabar_programa(contador_pares):
    
    print("Cantidad de números pares ingresados: {}".format(contador_pares))


def numeros_pares(num) -> bool:
             
        return num % 2 == 0


def main():

    contador_pares = 0
    num = intro_numero()
    while num != -1:

        suma = suma_num(num)
        print(f"La suma de los dígitos de {num} es: {suma}")


        if numeros_pares(num):
            
            contador_pares += 1
        
        num = intro_numero()

    acabar_programa(contador_pares)
    



if __name__ == "__main__":
    main()