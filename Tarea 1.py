#Quiero calcular los dias entre dos fechas       
dia1 = input("Dime un dia: ")
dia1=int(dia1)  
mes1 = input("Dime un mes: ")
mes1=int(mes1)
año1 = input("Dime un año: ")
año1=int(año1)
dia2 = input("Dime un dia: ")
dia2=int(dia2)
mes2 = input("Dime un mes: ")
mes2=int(mes2)
año2 = input("Dime un año: ")
año2=int(año2)
dias = abs((dia2-dia1)+((mes2-mes1)*30)+((año2-año1)*365))
print(f"Los dias entre las dos fechas son: {dias}")






