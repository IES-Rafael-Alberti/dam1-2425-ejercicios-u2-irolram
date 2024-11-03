#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

"""Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón."""

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

def pedir_pizza()-> str: 
    """
    Solicita al usuario si desea una pizza vegetariana o no y devuelve la respuesta.
    
    Returns:
        str: "vegetariana" si la pizza es vegetariana, "normal" en caso contrario.
    """
    print("Ingredientes vegetarianos: Pimiento y tofu. \nIngredientes no vegetarianos: Peperoni, Jamón y Salmón.")
    pizza = input("Quiere una pizza vegetariana o normal: ")

    return pizza.lower() 

def pizza_vege_ono(pizza):
    """
    Permite al usuario elegir ingredientes adicionales en función de su elección vegetariana o no vegetariana,
    y muestra el resultado con todos los ingredientes elegidos.
    
    Args:
        pizza (str): Tipo de pizza ("vegetariana" o "normal").
    """
    
    if pizza == "vegetariana":
        vegetariana = input("Introduzca su ingrediente extra: Pimiento y tofu.  ")
        while vegetariana != "pimiento" and "tofu":
            vegetariana = input("Introduzca su ingrediente extra: Pimiento y tofu.  ")
            print("La pizza vegetariana tiene los ingredientes siguientes:  Mozzarella, tomate y {}".format(vegetariana).lower())

    else:
        no_vege = input("Introduzca su ingrediente extra: Peperoni, Jamón y Salmón. ")
        while no_vege != "jamon" and "peperoni" and "salmon":
            no_vege = input("Introduzca su ingrediente extra: Peperoni, Jamón y Salmón.  ")
        print("La pizza tiene los ingredientes siguientes: Mozzarella, tomate y {}".format(no_vege).lower())
    

def main():

    pizza = pedir_pizza()
    pizza_vege_ono(pizza)


if __name__ == "__main__":
    main()