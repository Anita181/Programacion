#Pedir un texto, cuantas veces aparece cada palabra en el, convertir todo el texto en minuscula
texto = input("Ingresa un texo: ") #para pedirle algo al usuario
texto = texto.lower()  # para quitar las mayusculas
import re
texto_limpio = re.sub(r"[^\w\s]", "", texto) #para quitar signos de puntuacion
texto = texto_limpio.split()  # Separa la frase en una lista de palabras
frequencia_palabras = {} # diccionario vacio
for palabra in texto:  # recorremos cada palabra en la lista de palabras
    if palabra in frequencia_palabras:  # si la palabra esta en el diccionario que creamos
        frequencia_palabras[palabra] += 1  # si la palabra ya esta sumamos 1
    else:
        # si es nueva, la agregamos con valor 1
        frequencia_palabras[palabra] = 1

for palabra, frequencia in frequencia_palabras.items():  # separar las palabras en una columna
    print(f"{palabra}: {frequencia}") #para imprimir columnas


