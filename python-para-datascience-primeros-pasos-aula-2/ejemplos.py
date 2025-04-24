      print("w\nI\nL\nM\nE\nR")

a=10.56
b=5
texto=" Maria tine Pies de Reyna "
suma=a+b
resta=b-a
multiplica=a*b
divide=a/b

print("Variable a =",a, "y tipo ", type(a),
      "\nVariable b =", b, "y tipo ", type(b),
      "\nLa Variable suma = a+b igual a :", suma, "y tipo ", type(suma),
      "\nLa Variable resta = a-b igual a :", resta, "y tipo ", type(resta),
      "\nLa Variable multiplica = a*b igual a :", multiplica, "y tipo ", type(multiplica),
      "\nLa Variable divide = a/b igual a :", divide, "y tipo ", type(divide))


print (texto,"\nLa Variable texto es tipo :",type(texto),
       "\nEl id de memoria de la variable texto", id(texto))
texto=texto.replace("in","ien").strip().upper().replace("Y","I")
print(texto.lower())
print (texto)
print(texto.capitalize())
print ("El nuevo id de memoria de la variable texto es :", id(texto))

ano_admision=int(input("Digita año de admision : "))
ano_salida=int(input("Digita año de salida : "))
nota_admision=float(input("Digit la nota de admision : "))
print(f'\t\nEl año de admision fue : {ano_admision} \t\nLa nota de admision fue : {nota_admision} \t\nEl año de salida fue : {ano_salida}')
print(chr(72)+chr(111))
nombre = "Ana María"
edad = 17
print(f"El nombre de la alumna es {nombre} y su edad es {edad} años.")
nombre_alumno = 'Penélope Camacho'
edad_alumno = 11
media_alumno = 9.95
print('Nombre del alumno es %s, tiene %d años y su media es %f.' %(nombre_alumno, edad_alumno, media_alumno))
print('Nombre del alumno es %s, tiene %d años y su media es %.2f.' %(nombre_alumno, edad_alumno, media_alumno))
x = True
print("Valor de x: %s" % str(x))
nombre = input("Cual es tu nombre? ")
edad=int(input("cual es tu edad? "))
altura=float(input("Cuantos mides de altura? "))
print('Hola %s tienes %d años y mides %.2f metros de altura.' %(nombre, edad, altura))

edad_alumno = 15
media_alumno = 9.95
print('Nombre del alumno es {}, tiene {} años y su media es {}.' .format(nombre, edad_alumno, media_alumno))