#Convertir texto a mayúsculas y minúsculas
#frase = input("Escribe una frase: ")
#mayuscula = frase.upper()
#minuscula = frase.lower()
#print(mayuscula)
#print(minuscula)
#frase = input("Escribe una frase: ")
#frase_sin_espacios = frase.replace(" ", "") #contar letras sin espacios
#contador = len(frase_sin_espacios)
#print(("La frase tiene:", contador, "letras sin contar espacios"))
#frase = input("Escribe una frase: ")
#busca_palabra = input("Que palabra quieres buscar?: ")
#if busca_palabra in frase:
    #print("Si esta")
#else:
    #print("No la encontre")
#mini reto
frase = input("Escribe una frase: ")
mayuscula = frase.upper()
minuscula = frase.lower()
print("La frase en mayuscula:", mayuscula)
print("La frase en minuscula:", minuscula)
frase_sin_espacios = frase.replace(" ", "")
contador = len(frase_sin_espacios)
print(("La frase tiene:", contador, "letras sin contar espacios"))
busca_palabra = input("Que palabra quieres buscar?: ")
if busca_palabra in frase:
    print("Si esta")
else:
    print("No la encontre")