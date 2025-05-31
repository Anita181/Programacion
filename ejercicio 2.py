#PEDIR AL USUARIO QUE DIGA UNA FRASE, CONTAR CUANTAS PALABRAS TIENE E IMPRIMIRLO

frase = input("Escribe una frase: ") #para pedir al usuario algo
import re # Importamos la librería de expresiones regulares
frase_limpia = re.sub(r"[^\w\s]", "", frase) # Quitamos los signos de puntuación (.,!?)
palabras = frase_limpia.split()  # Separa la frase en una lista de palabras
num_palabras = len(palabras) #Cuenta cuantas palabras hay en la frase
print(f"La frase tiene {num_palabras} palabras.") #para imprimir el resultado de una variable


