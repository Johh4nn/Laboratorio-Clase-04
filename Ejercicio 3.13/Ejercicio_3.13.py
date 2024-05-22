import time 

costoPasaje = float(input("Ingrese la cantidad de alumnos que viajaran: "))
print("Calculando el precio del pasaje total")
print("por favor espere.....")

time.sleep (3)

if costoPasaje > 100 :
    costo = 20 * costoPasaje
    print(f'El precio final del pasaje: {costo}')
    
elif costoPasaje >=50 and costoPasaje <= 100 :
    costo = 35 * costoPasaje 
    print(f'El precio final del pasaje: {costo}') 
elif costoPasaje >=20 and costoPasaje <= 49 :
    costo = 40 * costoPasaje 
    print(f'El precio final del pasaje: {costo}') 

elif costoPasaje <= 20 :
    costo = 70 * costoPasaje 
    print(f'El precio final del pasaje: {costo}') 

else:
    print(f'El precio final del pasaje: {costo}')
