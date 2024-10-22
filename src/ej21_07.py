#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%"""

def pregunta_renta():

    renta =float(input("Introduzca su renta: "))

    return renta

def tipo_renta(renta):

    if renta < 10000:
        return print("Su impositivo es de un 5%")
    elif renta > 10000 and renta < 20000:
        return print("Su impositivo es de un 15%")
    elif renta > 20000 and renta < 35000:
        return print("Su impositivo es de un 20%")
    elif renta > 35000 and renta < 60000:
        return print("Su impositivo es de un 30%")
    elif renta > 60000:
        return print("Su impositivo es de un 45%")


def main():
    renta = pregunta_renta()
    tipo_renta(renta)



if __name__ == "__main__":
    main()