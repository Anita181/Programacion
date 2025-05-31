#Pide un numero entero positivo al usuario y luego imprima la tabla de multiplicar de ese número (del 1 al 10).

numero = int(input("Ingresa un numero: ")) #para solicitar un numero del usuario 
for i in range(1, 11): # i tomará valores del 1 al 10 
    resultado = numero * i #para multiplicar el numero por cada constante i
    print(f"{numero} x {i} = {resultado}")  #Para imprimir y que se vea bonito