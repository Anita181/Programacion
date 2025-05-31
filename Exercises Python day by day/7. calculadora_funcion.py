#Calculadora interactiva
def calcular(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "dividir":
        return num1 / num2
    else:
        return "Operación no válida"
seguir = "sí" #inicia el bucle
while seguir == "sí": #controla si se repite
    numero_1 = int(input("Dime el primer número: "))
    numero_2 = int(input("Dime el segundo número: "))
    operacion_final = input("¿Qué operación quieres hacer? (suma, resta, multiplicacion, dividir): ")

resultado = calcular(numero_1, numero_2, operacion_final)
print("El resultado es:", resultado)

seguir = input("¿Quieres hacer otra operación? (sí/no): ")#permite salir del bucle
