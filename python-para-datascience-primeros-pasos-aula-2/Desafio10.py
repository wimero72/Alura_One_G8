#10 - Un programa debe ser escrito para leer dos números y luego
#preguntar a la persona usuaria qué operación desea realizar. El
# resultado de la operación debe incluir información sobre el número,
# si es par o impar, positivo o negativo, e entero o decimal.

n1=(input("Introduzca el primer numero : "))
n2=(input("Introduzca el segundo numero : "))
oper=input("  1. Suma \n  2. Resta \n  3. Multiplicacion \n  4. Division \nDigita la operacion a efectuar de 1 a 4: ")

if oper=="1":
    if '.' in n1:
        n1 = float(n1)
        msg1="decimal"
        if n1%2==0:
            msg1+=", Par"
        else:
            print(n1 % 2)
            msg1+=", impar"

    elif n1.isdigit():
        n1=int(n1)
        msg1 = "entero"
        if n1 % 2==0:
            msg1 += ", Par"
        else:
            msg1 += ", impar"
    else:
        msg1=""
        print("Para el primer numero digite un valor numerico")

    if '.' in n2:
        n2 = float(n2)
        msg2 = "decimal"
        if n2 % 2==0:
            msg2 += ", Par"
        else:
            msg2 += ", impar"

    elif n2.isdigit():
        n2 = int(n2)
        msg2 = "entero"
        if n2 % 2==0:
            msg2 += ", Par"
        else:
            print(n1 % 2)
            msg2 += ", impar"
    else:
        msg2=""
        print("Para el segundo numero digite un valor numerico")

    if msg1=="" or msg2=="":
        print("vuelve a Intentarlo")
    else:
        print ("La suma de {} que es {} mas {} que es {} es igual a {}".format(n1,msg1, n2,msg2, (n1+n2)))
else:
    print("operacion invalida")
