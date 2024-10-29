#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

def pedir_compras():

    monto = int(input("Ingrese la compra articulo a articulo e ingrese 0 para acabar: "))

    return monto

def suma_articulos():
    """
        Realiza la suma total de los montos ingresados por el usuario para calcular el total a pagar.
    
    Proceso:
        - Solicita montos de compra uno por uno, hasta que el usuario ingrese 0.
        - Ignora montos negativos y solicita un nuevo monto si se ingresa uno negativo.
        - Si el monto acumulado supera $1000, aplica un descuento del 10%.
    
        Al finalizar, muestra el total a pagar con descuento si corresponde.

        
    """
    monto = pedir_compras()

    suma_total = 0

    while monto != 0:
       

        if monto < 0:
            print("ERROR, no sirven números negativos.")
            monto = pedir_compras()
        else:
            suma_total = suma_total + monto
        monto = pedir_compras()
    
    if suma_total > 1000:
        descuento = suma_total *0.10

        suma_total = suma_total - descuento

    

    if monto == 0:
        print("La compra total ha sido: {}".format(suma_total))


def main():

    suma_articulos()

if __name__ == "__main__":
    main()