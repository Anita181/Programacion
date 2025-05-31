#Listas
frutas = ["parchita", "fresa", "durazno", "cambur"]
print(frutas[2]) #imprime la fruta que esta en el segundo lugar
for fruta in frutas: #recorre fruta en la lista de frutas
    print(fruta)
frutas.append("piña") #agregar elemento de la lista
print(frutas)
frutas.remove("cambur") #quitar elemento de la lista
print(frutas)