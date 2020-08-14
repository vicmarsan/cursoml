""" 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
between 1500 and 2700 (both included). """

for numero in range(1500,2701):
    if numero % 7 == 0 and numero % 5 == 0:
        print(numero)

# Añadir , end=", " después de numero para separar los números según lo que se especifique entre "".

# Solución:

# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))

""" 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius """

# temp = input("Introduzca la temperatura que desea convertir (e.g., 45F, 102C etc.) : ")
# grados = int(temp[:-1])
# i_escala = temp[-1]

# try:
#     if i_escala == "C":
#         result = int((9 * grados) / 5 + 32)
#         o_escala = "Fahrenheit"
#     elif i_escala == "F":
#         result = int((grados - 32) * 5 / 9)
#         o_escala = "Celsius"   
# except ValueError: 
#         print ("Introduzca la escala correcta")

# print("La temperatura en", o_escala, "es", result, "grados.")

bien = False
o_convention = ""
result = 0
while not bien:


  temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
  try:
    degree = int(temp[:-1])
    i_convention = temp[-1]

    if i_convention.upper() == "C": # Pasarlo todo a mayúsculas con .upper. Minúsculas .lower,
                                    # .capital primera mayúscula, title la primera de cada palabra mayúscula.
      result = int(round((9 * degree) / 5 + 32))
      o_convention = "Fahrenheit"
      bien = True
    elif i_convention.upper() == "F":
      result = int(round((degree - 32) * 5 / 9))
      o_convention = "Celsius"
      bien = True
    else:
      print("Input proper convention.")
    if o_convention:  
      print("The temperature in", o_convention, "is", result, "degrees.")
    
  except ValueError:
    print("Escribe bien la temperatura")


