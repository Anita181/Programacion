# Sumar los números del 1 al 10.
suma = 0 #Creamos una “cajita” para guardar la suma
for numero in range(1, 11): #empieza en 1 y llega hasta 10 (el 11 no se incluye).
    suma = suma + numero #guarda en la cajita la suma de lo que ya había + el nuevo número.
print("La suma del 1 al 10 es:", suma)

suma = 0 #Creamos una “cajita” para guardar la suma
for numero in range(1, 101): #empieza en 1 y llega hasta 100 (el 101 no se incluye).
    suma = suma + numero #guarda en la cajita la suma de lo que ya había + el nuevo número.
print("La suma del 1 al 100 es:", suma)