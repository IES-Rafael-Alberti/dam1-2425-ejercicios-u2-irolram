#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

def introducir_numero():

    num= int(input("Introduce un número: "))

    return num

def comprobar_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
         if num % i == 0:
            return False
    return True 
    
def main():
    num = introducir_numero()
    if comprobar_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
    

if __name__ == "__main__":
    main()