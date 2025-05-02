#10 - Un programa debe ser escrito para leer dos números y luego
#preguntar a la persona usuaria qué operación desea realizar. El
#resultado de la operación debe incluir información sobre el número,
#si es par o impar, positivo o negativo, e entero o decimal.

n1=float(input("Introduzca el primer numero : "))
n2=float(input("Introduzca el segundo numero : "))
oper=input("  1. Suma \n  2. Resta \n  3. Multiplicacion \n  4. Division \nDigita la operacion a efectuar de 1 a 4: ")

try: 
    if n1.is_integer() or isinstance(n1, float) and n2.is_integer() or isinstance(n2, float):
        try:
            #Validacion del primer numero
            operar=True
            if n1.is_integer():
                n1 = int(n1)
                print("n1 Entero")
                if n1>0:
                    msg1="Positivo"
                elif n1<0:
                    msg1="Negativo"
                else:
                    msg1="Cero"
                msg1+=", Entero"
                if n1%2==0:
                    msg1+=", Par"
                else:
                    msg1+=", Impar"
            elif isinstance(n1, float):
                n1 =  float(n1)
                print("n1 decimal")
                if n1>0:
                    msg1="Positivo"
                elif n1<0:
                    msg1="Negativo"
                else:
                    msg1="Cero"
                msg1+=", Decimal"
                if n1 % 2==0:
                    msg1 += ", Par"
                else:
                    msg1 += ", Impar"
        except:
            operar=False
            print("Para el primer numero digite un valor numerico")       
        try:            
            #Validacion del segundo numero
            operar=True
            if n2.is_integer():
                n2 = int(n2)
                print("n2 entero")
                print(n2)
                if n2>0:
                    msg2="Positivo"
                elif n2<0:
                    msg2="Negativo"
                else:
                    msg2="Cero"
                msg2 += ", Entero"
                if n2 % 2==0:
                    msg2 += ", Par"
                else:
                    msg2 += ", Impar"

            elif isinstance(n2, float):
                n2 =  float(n2)
                print("n2 decimal")
                if n2>0:
                    msg2="Positivo"
                elif n2<0:
                    msg2="Negativo"
                else:
                    msg2="Cero"
                msg2+=", Decimal"
                if n2 % 2==0:
                    msg2 += ", Par"
                else:
                    msg2 += ", Impar"
        except:
            operar=False
            print("Para el segundo numero digite un valor numerico")
                
except:
    operar=False
#Menu de Operacion a ejecutar con los dos numero
if oper=="1" and operar:
    oper_desc="mas (+)"
    result=n1+n2 #Ejecutando operacion Suma
elif oper=="2" and operar:
    oper_desc="menos (-)"
    result=n1-n2 #Ejecutando operacion Resta
elif oper=="3" and operar:
    oper_desc="multiplicado (*)"
    result=n1*n2 #Ejecucion operacion Multiplicacion
elif oper=="4" and operar:
    oper_desc="dividido (÷)"
    if n2!=0:
        result= (n1/n2) #Ejecucion operacion Division
    else:
        operar=False 
else:
    print("Operacion Invalida")
#oper=""
#print("los valores introducidos deben ser numericos, y los decimales separados por punto (.) en ves de coma(,)")
#Impresion del resultado de la Resta y caracteristicas numericas de cada numero intriducido
if operar:
    msg4="es un numero"
    if result.is_integer():
        result=int(result)
        msg3 = "Entero"
        if result>0:
           msg3+=", Positivo"
        elif result<0:
           msg3+=", Negativo"
        else:
           msg3+=", Cero"
        if  result % 2==0:
           msg3+=", Par"
        else:
           msg3+=", Impar"
    else:
        msg4="es un numero"
        msg3 = "Decimal"
        if result>0:
           msg3+=", Positivo"
        elif result<0:
           msg3+=", Negativo"
        else:
           msg3+=", Cero"
        if  result % 2==0:
           msg3 += ", Par"
        else:
           msg3 += ", Impar"
else:
    msg3=""
    msg4="Division entre 0"
    print("Vuelve a Intentarlo")
  
print ("El primer numero ({}), es {}, {}, \nEl segundo numero ({}) es {} \nigual (=) a ({}) {}".format(n1, msg1, oper_desc, n2, msg2, ("X" if operar==False else result), ((msg4+" "+msg3) if msg4!="" else msg4)))