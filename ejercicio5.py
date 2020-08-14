palabra = input("Escribe una palabra: ")
longitud = len(palabra)

for posicion in range(longitud - 1, -1, -1):
    print(palabra[posicion], end = "")
print("")


str = "" 
for i in palabra: 
    str = i + str
print(str)

