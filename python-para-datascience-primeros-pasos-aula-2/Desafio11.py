#11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo.
# El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, 
# si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias: 
#Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero; 
#Triángulo Equilátero: tres lados iguales; 
#Triángulo Isósceles: dos lados iguales; 
#Triángulo Escaleno: tres lados diferentes. 

n1=float(input("Introduzca el primer numero : "))
n2=float(input("Introduzca el segundo numero : "))
n3=float(input("Introduzca el tercer numero : "))

if n1+n2>n3 and n2+n3>n1 and n3+n1>n2:
    print("Es un traiangulo ")
    msg= "Equilatero" if n1==n2==n3 else msg 
    

elif: