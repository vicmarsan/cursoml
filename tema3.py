"""
Esta parte es para
la gestión de errores con try-except
"""

# year = input("dime en qué año naciste: ")
# print("naciste en", year)
# numero = 2
# try:
#     print(int(year) + numero)
# except ValueError: 
#     print ("no seas tonto , los años no tienen letras")



"""
Ejemplo de while, con y sin bucle infinito
"""
inicio = 10
fin = 3
while inicio > fin:
    print(inicio)
    inicio = inicio - 1

print("acabo")




"""
Ejemplo de for
"""

clase= {   "manolo":15,
"juan"  :22,
"antonio": 45,
"rafa": 21,
"gema": 24,
"vicky": 20

}

year= 2020
for alumno in clase:
    print(alumno, "nació en", year - clase[alumno])

for letra in "España":
    print(letra)

meses = ("enero", "febrero", "marzo", "abril", "mayo")

for mes in meses:
    if mes[0] == "m":
        print(mes)


for numero in range(3, 11, 2):
    print(numero)


a=5
a, b = 5, 8