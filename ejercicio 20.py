#Pedir al usuario una frase y contar cuántas palabras empiezan con la letra "m" (puede ser mayúscula o minúscula).
frase = input("Escribe una frase: ")
frase.split() #divide la frase en una lista de palabras.
contar_palabras = 0
palabras_con_m = []  # Lista para guardar las palabras que empiezan con 'm'
for palabra in frase.split(): #significa que estamos recorriendo cada palabra de esa lista.
    if palabra[0].lower() == "m": #obtiene la primera letra de cada palabra, convierte esa letra a minúscula, para que no importe si es "M" o "m", compara si esa letra es igual a "m".
        contar_palabras += 1
        palabras_con_m.append(palabra)  # Añadimos la palabra a la lista
print("La cantidad de palabras que empiezan con M es:", contar_palabras)
print("Las palabras que empiezan con 'm' son:", palabras_con_m)

