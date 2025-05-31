#Pide un texto del usuario y cuente: Cuántas letras tiene el texto, Cuántos números hay, Cuántos espacios hay, Cuántos signos de puntuación hay (como . , ! ? ; :).
texto = input("Escribe un texto: ")
contador_letras = 0 #variables donde vamos a contar las letras
contador_numeros = 0
contador_espacios = 0
signos_puntuacion = ".,¡!¿?;:"  # Los signos que queremos contar
contador_signos = 0
for caracter in texto: #para recorrer el texto
    if caracter.isalpha():  # Si es una letra...
        contador_letras += 1  # Sumar uno al contador
    if caracter.isdigit():  # Si es un número...
        contador_numeros += 1  # Sumar uno al contador de números
    if caracter == " ":  # Si es un espacio...
        contador_espacios += 1  # Sumar uno al contador de espacios
    if caracter in signos_puntuacion:  # Si es uno de esos signos...
        contador_signos += 1  # Sumar uno al contador de signos
print("Número de letras:", contador_letras)
print("Cantidad de Números:", contador_numeros)
print("Cuantos espacios tiene:", contador_espacios)
print("Cuantos signos de puntuacion tiene:", contador_signos)