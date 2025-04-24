#8 - Escribe un programa que solicite un número entero a la persona usuaria y determine si es par o impar. Pista: 
# Puedes usar el operador módulo (%).
numero= int(input("Digite un número entero: "))
if numero==0:
    print("El número es cero.")
elif numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
    