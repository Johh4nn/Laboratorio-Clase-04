#delcaracion de contantes 
import time 


#ingreso de datos 

def espera():
    print("Espere calculando...")
    time.sleep(3)


print("UIOTOVINO")
print("")
tipo = input("Ingrese el tipo de Uva A o B: ")
tama = int(input("Ingrese el tamaño de la uva sea 1 o 2: "))
peso = float(input("Ingrese el peso: "))
precio = float(input("Ingrese el valor por kilo: "))


preciok = float(precio*peso) 


if tipo == "A" and tama == 1:
    espera();
    preciof = float(preciok+0.20)
    print("")
elif tipo == "A" and tama == 2 :
    espera();
    preciof = float(preciok+0.50)
    print("")
elif tipo == "B" and tama == 1 :
    espera();
    preciof = float(preciok-0.30)
    print("")
else :
    espera();
    preciof = float(preciok-0.50)
    print("")

#Salida de datos 
print(f"El precio inicial calculado es : {preciok}")
print(f"El precio final ah pagar es: {preciof}")
