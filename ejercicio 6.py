#Crea un programa que reciba un número entero positivo n e imprima una lista con los números del 1 al n

n = int(input("Escribe un numero: "))  #para solicitar un numero del usuario 
resultado = []  # Lista vacía
for i in range(1, n + 1): #Recorremos del 1 hasta n
    if i % 3 == 0 and i % 5 == 0:  # Si es múltiplo de 3 y 5
        resultado.append("FizzBuzz") # para agregar elementos a una lista. 
    elif i % 3 == 0:  # Si es múltiplo de 3
        resultado.append("Fizz")
    elif i % 5 == 0:  # Si es múltiplo de 5
        resultado.append("Buzz")
    else:  # Si no es múltiplo ni de 3 ni de 5, agregamos el número
        resultado.append(i)
print(resultado)  # Mostramos la lista final