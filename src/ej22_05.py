#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

"""
# Formula para calcular El capital tras un año.
cantidad *= 1 + interes / 100
# En donde:
# - cantidad: Cantidad a invertir
# - interes: Interes porcentual anual 
"""

def preguntar_cantidad_invertir():
    """
    Solicita al usuario la cantidad a invertir, el número de años y el interés anual.

    Returns:
        tuple: Contiene la cantidad a invertir (float), la cantidad de años (int) y el interés anual (float).
    """
    cantidad = float(input("Ingrese la cantidad a invertir: "))
    anios = int(input("Ingrese la cantidad de años: "))
    interes = int(input("Introduce el interes anual: "))

    return cantidad, anios, interes


def capital(cantidad, anios, interes):
    """
    Calcula el capital acumulado durante un número de años dado un interés anual.

    Args:
        cantidad (float): La cantidad inicial a invertir.
        anios (int): El número de años que se va a invertir.
        interes (float): El interés anual expresado como una fracción (por ejemplo, 0.05 para 5%).
    """

    cont = 0
    for i in range(1, anios +1 ):
        cont = cont + 1
        cantidad *= (1 + interes)
        print("año {} su inversión es de {}".format(cont,cantidad))
        

def main():

    cant, anios, interes =preguntar_cantidad_invertir()
    capital(cant, anios, interes)





if __name__ == "__main__":
    main()