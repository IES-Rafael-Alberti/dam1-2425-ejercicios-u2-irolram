#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
"""
Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
"""
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario

def puntuacion():

    punt= float((input("Introduce la puntuación: ")))

    return punt

def calculo_puntuacion(punt):

    if punt == 0.0:
        punt = (2400 * 0.0) + 2400
        return print("Has ganado {}€ y tú Nivel es Inaceptable, mejora".format(punt))

    elif punt == 0.4:
        punt = (2400 * 0.4) + 2400
        return print("Has ganado {}€ y tú actitud es Aceptable, se puede mejorar".format(punt))

    elif punt == 0.6:
        punt = (2400 * 0.6) + 2400
        return print("Has ganado {}€ y tú actitud es Meritorio, bien".format(punt))



def main():
     punt = puntuacion()
     calculo_puntuacion(punt)


if __name__ == "__main__":
    main()