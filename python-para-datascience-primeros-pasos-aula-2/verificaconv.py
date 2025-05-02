a = float(input("digita un valor1 : "))
b = float(input("digita un valor2 : "))
print(type(a)) # Output: <class 'float'>
print(type(b)) # Output: <class 'float'>
print(a.is_integer())
print(b.is_integer())
#print(a.is_float())
#print(b.is_float())

print("a es entero?", isinstance(a, int))  # Output: False
print("a es decimal?",isinstance(a, float))  # Output: True

print("b es entero?", b, isinstance(b, int))  # Output: False
print("b es decimal?", b, isinstance(b, float))  # Output: True