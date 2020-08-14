
bien = False

while not bien:
    year = input("dime en qué año naciste: ")
    print("naciste en", year)
    numero = 2
    try:
      print(int(year) + numero)
      bien = True
    except ValueError: 
      print ("no seas tonto , los años no tienen letras")


