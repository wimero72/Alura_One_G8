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


print (texto, 
       "\nLa Variable texto es tipo :",type(texto),
       "\nEl id de memoria de la variable texto", id(texto))
texto=texto.replace("in","ien").strip().upper().replace("Y","I")
print(texto.lower())
print (texto)
print(texto.capitalize())
print ("El nuevo id de memoria de la variable texto es :", id(texto))

ano_admision=int(input("Digita año de admi¡sion : "))
ano_salida=int(input("Digita año de salida : "))
nota_admision=float(input("Digit la nota de admision : "))
print(f'\t\nEl año de admision fue : {ano_admision} \t\nLa nota de admision fue : {nota_admision} \t\nEl año de salida fue : {ano_salida}')
print(chr(72))