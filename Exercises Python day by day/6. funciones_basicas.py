# Funciones con parámetros y return
def sumar(num1, num2):  # Crea una función llamada sumar, que reciba 2 numeros
    resultado = num1 + num2
    return resultado  # Que devuelva la suma con return.


suma = sumar(3, 5)
print("La suma es:", suma)


def es_par(numero):
    if numero % 2 == 0:
        return "es par"
    else:  # en caso contrario
        return "es impar"

valor_final = es_par(3)
print(valor_final)
