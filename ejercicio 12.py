#Escribe un programa que cuente cuántas palabras hay en una frase ingresada por el usuario.
frase = input("Escribe una frase: ")
palabras = frase.split() #Esto creará una lista con cada palabra de la frase. 
cantidad_palabras = len(frase.split()) #cuenta las palabras
print(f'La frase tiene: {cantidad_palabras} palabras')