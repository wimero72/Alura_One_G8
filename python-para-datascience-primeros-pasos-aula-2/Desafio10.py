#10 - Un programa debe ser escrito para leer dos números y luego
#preguntar a la persona usuaria qué operación desea realizar. El
# resultado de la operación debe incluir información sobre el número,
# si es par o impar, positivo o negativo, e entero o decimal.

n1=(input("Introduzca el primer numero : "))
n2=(input("Introduzca el segundo numero : "))
oper=input("  1. Suma \n  2. Resta \n  3. Multiplicacion \n  4. Division \nDigita la operacion a efectuar de 1 a 4: ")
#Operacion a ejecutar con el primer y segundo numero
#Validacion de la opcion operacopm Resta
if oper=="1":
    #Validacion de primer numero
    if '.' in n1:
        n1 = float(n1)
        msg1="Decimal"
        if n1>0:
            msg1+=", Positivo"
        elif n1<0:
            msg1+=", Negativo"
        else:
            msg1+=", Cero"
        if n1%2==0:
            msg1+=", Par"
        else:
            print(n1 % 2)
            msg1+=", Impar"

    elif n1.isdigit():
        n1=int(n1)
        msg1 = "Entero"
        if n1>0:
            msg1+=", Positivo"
        elif n1<0:
            msg1+=", Negativo"
        else:
            msg1+=", Cero"
        if n1 % 2==0:
            msg1 += ", Par"
        else:
            msg1 += ", Impar"
            
    #Validacion del segundo numero
    if '.' in n2:
        n2 = float(n2)
        msg2 = "Decimal"
        if n2>0:
            msg2+=", Positivo"
        elif n2<0:
            msg2+=", Negativo"
        else:
            msg2+=", Cero"
        if n2 % 2==0:
            msg2 += ", Par"
        else:
            msg2 += ", Impar"

    elif n2.isdigit():
        n2 = int(n2)
        msg2 = "Entero"
        if n2>0:
            msg2+=", Positivo"
        elif n2<0:
            msg2+=", Negativo"
        else:
            msg2+=", Cero"
        if n2 % 2==0:
            msg2 += ", Par"
        else:
            print(n1 % 2)
            msg2 += ", Impar"
    else:
        msg2=""
        print("Para el segundo numero digite un valor numerico")

#Impresion del resultado de la Suma y caracteristicas numericas de cada numero y el resultado
    if msg1=="" or msg2=="":
        print("vuelve a Intentarlo")
    else:
        print ("El primer numero ({}), es un numero {}, mas (+), \nEl segundo numero ({}) es un numero {} \nigual (=) a ({})".format(n1,msg1, n2,msg2, (n1+n2)))
else:
    print("Operacion Invalida")
    
#Validacion de la opcion operacopm Resta
if oper=="2":
    #Validacion del Primer numero intruducido
    if '.' in n1:
        n1 = float(n1)
        msg1="Decimal"
        if n1>0:
            msg1+=", Positivo"
        elif n1<0:
            msg1+=", Negativo"
        else:
            msg1+=", Cero"
        if n1%2==0:
            msg1+=", Par"
        else:
            print(n1 % 2)
            msg1+=", Impar"

    elif n1.isdigit():
        n1=int(n1)
        msg1 = "Entero"
        if n1>0:
            msg1+=", Positivo"
        elif n1<0:
            msg1+=", Negativo"
        else:
            msg1+=", Cero"
        if n1 % 2==0:
            msg1 += ", Par"
        else:
            msg1 += ", Impar"
            
    else:
        msg1=""
        print("Para el primer numero digite un valor numerico")

    #Validacion del Segundo numero introducido
    if '.' in n2:
        n2 = float(n2)
        msg2 = "Decimal"
        if n2>0:
            msg2+=", Positivo"
        elif n2<0:
            msg2+=", Negativo"
        else:
            msg2+=", Cero"
        if n2 % 2==0:
            msg2 += ", Par"
        else:
            msg2 += ", Impar"

    elif n2.isdigit():
        n2 = int(n2)
        msg2 = "Entero"
        if n2>0:
            msg2+=", Positivo"
        elif n2<0:
            msg2+=", Negativo"
        else:
            msg2+=", Cero"
        if n2 % 2==0:
            msg2 += ", Par"
        else:
            print(n1 % 2)
            msg2 += ", Impar"
    else:
        msg2=""
        print("Para el segundo numero digite un valor numerico")
        
#Impresion del resultado de la Resta y caracteristicas numericas de cada numero intriducido
    if msg1=="" or msg2=="":
        print("vuelve a Intentarlo")
    else:
        print ("El primer numero ({}), es un numero {}, mas (-), \nEl segundo numero ({}) es un numero {} \nigual (=) a ({})".format(n1, msg1, n2, msg2, (n1-n2)))
else:
    print("Operacion Invalida")