5#3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.
letra = input("Digite una letra: ").lower()
if letra in "aeiou":
    print("La letra es una vocal.")
elif letra.isalpha():
    print("La letra es una consonante.")
else:
    print("El caracter igresado no es válido como letra.")
