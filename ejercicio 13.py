#reciba una oración del usuario y cuente cuántas palabras tiene. No debes considerar signos de puntuación como puntos, comas o signos de exclamación.
oracion = input("Escribre una oracion: ")
import re # Importamos la librería de expresiones regulares
oracion_limpia = re.sub(r"[^\w\s]", "", oracion) # Eliminamos cualquier carácter que no sea una letra o un espacio
palabras = oracion_limpia.split()  # Separa la frase en una lista de palabras
num_palabras = len(palabras) #Cuenta cuantas palabras hay en la frase
print(f"La oracion tiene {num_palabras} palabras.") #para imprimir el resultado de una variable
