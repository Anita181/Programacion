# Un programa que recorra una lista de números y muestre solo los números pares.

numeros = [3, 10, 7, 18, 25, 22, 30]  # lista de numeros
for numero in numeros:  # recorremos cada numero en la lista de numero con for
    if numero % 2 == 0: # para ver si el número es par.
        print(numero)   # si es par lo imprimimos
    
