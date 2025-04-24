#6 - Escribe un programa que lea tres números y los muestre en orden descendente.
# Leo tres números del usuario
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

# Compararo Los números y los muestro en orden descendente usando IF, ELIF, ELSE
if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print("Números en orden descendente:", n1, n2, n3)
    else:
        print("Números en orden descendente:", n1, n3, n2)
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print("Números en orden descendente:", n2, n1, n3)
    else:
        print("Números en orden descendente:", n2, n3, n1)
else:
    if n1 >= n2:
        print("Números en orden descendente:", n3, n1, n2)
    else:
        print("Números en orden descendente:", n3, n2, n1)

