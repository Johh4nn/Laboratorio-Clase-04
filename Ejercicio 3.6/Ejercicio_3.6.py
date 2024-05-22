#Presentación del programa
print ("----Bienvenido, este programa está diseñado para" "\n" 
       "determinar el costo y el descuento que tendrá un artículo----" "\n")
#Datos de entrada 
precio = float (input("Ingrese el valor total de los productos: "))
if precio >= 200:
    precio_descuento = (0.15 * precio)
    precio_final = precio - precio_descuento
    print (f"El valor a pagar es de: {round(precio_final,2)}, ya que usted" 
           "\n""tiene un descuento de 15%")
elif precio > 100 and precio < 200:
    precio_descuento = (0.12 * precio)
    precio_final = precio - precio_descuento
    print (f"El valor a pagar es de: {round(precio_final,2)}, ya que usted" 
           "\n""tiene un descuento de 12%")
else:
    precio_descuento = (0.10 * precio)
    precio_final = precio - precio_descuento
    print (f"El valor a pagar es de: {round(precio_final,2)}, ya que usted" 
           "\n""tiene un descuento de 10%")
