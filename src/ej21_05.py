#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no

def preguntas():

    edad = int(input("Introduce tu edad: "))
    ingresos = int(input("Introduzca el ingreso: "))

    return edad, ingresos

def comprobar_casos(edad,ingresos):
    if edad > 16 and ingresos > 1000:
        print("A tributar")
    else:
        print("No puedes tributar")

def main():
    edad, ingresos = preguntas()
    comprobar_casos(edad, ingresos)

    
if __name__ == "__main__":
    main()