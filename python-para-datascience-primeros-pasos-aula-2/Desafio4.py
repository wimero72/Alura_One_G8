#4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos
# y muestre el valor más alto y más bajo entre esos tres años.
contador=1

valor_prome_ano1 = float(input("Digita el valor promedio del Mazda SUB CX9 del primer año consecutivo : "))
valor_prome_ano2 = float(input("Digita el valor promedio del Mazda SUB CX9 del segundo año consecutivo : "))
valor_prome_ano3 = float(input("Digita el valor promedio del Mazda SUB CX9 del tercer año consecutivo : "))

if valor_prome_ano1 > valor_prome_ano2 and valor_prome_ano1 > valor_prome_ano3:
    if valor_prome_ano2>valor_prome_ano3:
        print("El valor promedio del 1er año consecutivo es el mayor %.2F y el del 3er año es el menor : %.2f " % (valor_prome_ano1, valor_prome_ano3))
    else:
        print("El valor promedio del 1er año consecutivo es el mayor %.2F y el del 2er año es el menor : %.2f " % (valor_prome_ano1, valor_prome_ano2))
elif valor_prome_ano1 == valor_prome_ano2 and valor_prome_ano2== valor_prome_ano3:
    print("El valor promedio no cambio en los tres ultimos años : %.2F" % valor_prome_ano2)
elif valor_prome_ano2>valor_prome_ano3:
    print("El valor promedio de 2do año consecutivo es el mayor %.2F" % valor_prome_ano3)
else:
    print("El valor promedio de 3er año consecutivo es el mayor %.2F" % valor_prome_ano3)