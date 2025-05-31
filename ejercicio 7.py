#Escribir un programa que cuente cuántas vocales (a, e, i, o, u) hay en una palabra dada. 
palabra = input("Escribe una palabra: ") # El usuario ingresa la palabra
cuenta_vocales = 0 # Variable para contar las vocales
for letra in palabra:   # Recorremos cada letra de la palabra
    if letra in "aeiou": # Si la letra es una vocal
        cuenta_vocales += 1  # Aumentamos el contador
print("Número de vocales:", cuenta_vocales)  # Mostramos el resultado
