#2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e informe si hubo un crecimiento (porcentaje positivo) 
# o una disminución (porcentaje negativo).

Porcentaje = float(input("Digite el porcentaje de crecimiento de producción de la empresa: "))
if Porcentaje > 0:
    print("Hubo un crecimiento de producción del", Porcentaje, "%")
elif Porcentaje < 0:
    print("Hubo una disminución de producción del", Porcentaje, "%")
else:
    print("No hubo cambios en la producción de la empresa.")