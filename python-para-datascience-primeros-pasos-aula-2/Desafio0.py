contador=1
while contador<=3:
    nota1=float(input("Digita la primera nota : "))
    nota2=float(input("Digita la segunda nota : "))
    print("La nota promedio del estudiante %d es : %.2f" % (contador,(nota1+nota2)/2))
    contador+=1
    
for e in range(1,4):
    nota1=float(input("Digita la primera nota : "))
    nota2=float(input("Digita la segunda nota : "))
    print("La nota promedio del estudiante %d es : %.2f" % (e,(nota1+nota2)/2))
    