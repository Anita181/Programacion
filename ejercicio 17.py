#Cuenta cuántas letras mayúsculas hay en una palabra o frase.
frase = input("Escribe una frase: ")
cuenta_mayusculas = 0
for letra in frase:
    cuenta_mayusculas += letra.isupper()
print("La frase tiene", cuenta_mayusculas, "mayusculas")

