#7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", "tarde" o "noche") 
# y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.
#leo las variable jornada del usuario
jornada = input("¿En qué turno estudias? (mañana, tarde o noche): ").strip().lower()
if jornada == "mañana":
    print("¡Buenos Días!")
elif jornada == "tarde":
    print("¡Buenas Tardes!")
elif jornada == "noche":
    print("¡Buenas Noches!")
else:
    print("Valor Inválido!")