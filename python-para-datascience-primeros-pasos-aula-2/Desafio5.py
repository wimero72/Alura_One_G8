#5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.
producto1=float(input("Digite el valor del primer producto : "))
producto2=float(input("Digite el valor del segundo producto : "))
producto3=float(input("Digite el valor del tercer producto : "))
if producto1<producto2 and producto1<producto3:
    print("El producto 1 es el mas barato : %.2f" % producto1)
elif producto2<producto3 and producto2<producto1:
    print("El producto 2 es el mas barato : %.2f" % producto2)
elif producto1==producto2 and producto2==producto3:
    print("Los tres productos tienen el mismo precio : %.2f" % producto1)
else:
    print("El producto 3 es el mas barato : %.2f" % producto3)