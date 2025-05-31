#Listas
#frutas = ["parchita", "fresa", "durazno", "cambur"]
#print(len(frutas))#contar cuantas frutas hay
#frutas.sort()#ordenar alfabeticamente
#print(frutas)
#frutas.insert(4, "frambuesa")#para poner elementos donde quieras
#print(frutas)
frutas = ["parchita", "fresa", "durazno", "cambur"]
nueva_fruta = input("Escribe una fruta para agregar al final: ").strip()
frutas.append(nueva_fruta)
otra_fruta = input("Escribe otra fruta para agregar al principio: ").strip()
frutas.insert(0, otra_fruta)
frutas.sort()
print("Lista final ordenada:", frutas)