#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

from ej21_01  import preguntar_edad


def todos_anios_cumplido(edad):
    """
    Muestra todos los años que el usuario ha cumplido hasta su edad actual.
    
    Args:
        edad (int): La edad del usuario.
    """
    guardar_edad = ""

    for i in range(1, edad + 1):
        guardar_edad += str(i) + ", "
        if i == edad:
            guardar_edad = guardar_edad.removesuffix(", ")

    print("Has cumplido los siguientes años: {}".format(guardar_edad))
    


def main():
    edad = preguntar_edad()
    todos_anios_cumplido(edad)

if __name__ == "__main__":
    main() 