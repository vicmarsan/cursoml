from datetime import datetime


dia_nacimiento = input("Escribe tu fdía de nacimiento: ")
mes_nacimiento = input("Escribe tu fecha de nacimiento (año, mes, día): ")
año_nacimiento = input("Escribe tu fecha de nacimiento (año, mes, día): ")

hoy = datetime.now()
nacimiento_string = dia_nacimiento + mes_nacimiento + año_nacimiento
nacimiento = datetime.strptime(nacimiento_string, "%d%m%Y")

cumpleaños_string = dia_nacimiento + mes_nacimiento + str(hoy.year)
cumpleaños = datetime.strptime(cumpleaños_string, "%d%m%Y")
if hoy > cumpleaños:
    cumpleaños_string = dia_nacimiento + mes_nacimiento + str(hoy.year + 1)
    cumpleaños = datetime.strptime(cumpleaños_string, "%d%m%Y")
days = cumpleaños - hoy 

print(days.days)


