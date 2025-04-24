#9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.
numero = input("Digite un número: ")
if '.' in numero or ',' in numero: 
  print("El número es decimal.")
else:
  print("El número es entero.") 

if numero.isdigit(): 
  print("Con isdigit. El número es entero.")
else:
  print("Con isdigit. El número es decimal.") 