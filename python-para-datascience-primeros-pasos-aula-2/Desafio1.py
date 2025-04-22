#1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
num1=int(input("Digite el primer numero: "))
num2=int(input("Digite el segundo numero: "))
if num1>num2:
    print("El numero mayor es: ",num1)
elif num2>num1:
    print("El numero mayor es: ",num2)
else:
    print("Los numeros son iguales")