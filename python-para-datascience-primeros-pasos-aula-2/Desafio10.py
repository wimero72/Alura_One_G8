#10 - Un programa debe ser escrito para leer dos números y luego
#preguntar a la persona usuaria qué operación desea realizar. El
# resultado de la operación debe incluir información sobre el número,
# si es par o impar, positivo o negativo, e entero o decimal.

n1=(input("Introduzca el primer numero : "))
n2=(input("Introduzca el segundo numero : "))

result=0
if n1.isdigit() or '.' in n1 or '-' and n2.isdigit() or '.' in n2 or '-':
        #Menu de Operacion a ejecutar con los dos numero
        oper=input("  1. Suma \n  2. Resta \n  3. Multiplicacion \n  4. Division \nDigita la operacion a efectuar de 1 a 4: ")
        
        #Validacion de la opcion operacopm Suma
        if oper=="1":
            oper_desc="mas (+)"
            #Validacion de primer numero de la Suma
            if '.' in n1 and '-' in n1 or "." in n1:
                n1 = float(n1)  
                result = n1
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

            elif "-" in n1 or n1.isdigit():
                n1 =  int(n1)
                result = n1
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
                    
            #Validacion del segundo numero de la Suma
            if '.' in n2:
                n2 = float(n2)
                result += n2
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
                n2 =  int(n2)
                result += n2
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
            
         #Validacion de la opcion operacion Resta
        elif oper=="2":
            oper_desc="menos (-)"
            #Validacion de primer numero de la Resta
            if '.' in n1:
                n1 = float(n1)  
                result = n1
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
                n1 =  int(n1)
                result = n1
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
                    
            #Validacion del segundo numero de la Resta
            if '.' in n2:
                n2 = float(n2)
                result -= n2
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
                n2 =  int(n2)
                result -= n2
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
                
          #Validacion de la opcion operacion Multiplicaion
        elif oper=="3":
            oper_desc="multiplicado (*)"
            #Validacion de primer numero de la Multiplicacion
            if '.' in n1:
                n1 = float(n1)  
                result = n1
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
                n1 =  int(n1)
                result = n1
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
                    
            #Validacion del segundo numero de la Multiplicacion
            if '.' in n2:
                n2 = float(n2)
                result *= n2
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
                n2 =  int(n2)
                result *= n2
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
                
                
        else:
            print("Operacion Invalida")
else:
    oper=""
    print("los valores introducidos deben ser numericos, y los decimales separados por punto (.) en ves de coma(,)")

print(result)            
#Impresion del resultado de la Resta y caracteristicas numericas de cada numero intriducido
if result==0 and oper=="":
    print("vuelve a Intentarlo")
else:
    if type(result) == int:
        msg3 = "Entero"
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
    
    print ("El primer numero ({}), es un numero {}, {}, \nEl segundo numero ({}) es un numero {} \nigual (=) a ({}) es un numero {}".format(n1, msg1, oper_desc, n2, msg2, result, msg3))