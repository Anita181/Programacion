#Contar cuántos números pares hay en una lista
numeros = [28, 11, 88, 23, 1, 51, 11, 1, 86] #lista de numeros
contador_pares = 0
for numero in numeros:
    if numero % 2 == 0: #si el numero es par
        print(numero)
        contador_pares += 1
print("Hay", contador_pares, "numeros pares en la lista")