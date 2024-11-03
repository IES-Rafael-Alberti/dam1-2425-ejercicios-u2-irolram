#algoritmo burbuja

lista_num = [5,3,20,15,2,1]

for i in range(len(lista_num)):
    #Comparamos lo que hay en una lista con los bucles
    for j in range(0, len(lista_num) - i - 1):
        #Si el primer número que se compara es mayor que el segundo, se cambiaran la posición
        if lista_num[j] > lista_num[j + 1]:
            lista_num[j], lista_num[j + 1] = lista_num[j + 1], lista_num[j]

print(lista_num)