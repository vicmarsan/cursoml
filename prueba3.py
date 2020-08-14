# import ejemplo_funciones
from datetime import datetime

from ejemplo_funciones import sacar_datetime

print (ejemplo_funciones.dia_tonto)

# fecha_hecha = ejemplo_funciones.sacar_datetime("02", "07")
fecha_hecha = sacar_datetime("02", "07")

print(fecha_hecha)
print(datetime.strftime(fecha_hecha, "%A"))
Thursday