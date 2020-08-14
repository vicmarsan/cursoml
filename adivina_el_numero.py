import random

numero = random.randrange(1, 10)
guess = int(input("Adivina el número del 1 al 9: "))

while guess > 9 or guess < 1:
    print("El número tiene que estar entre 1 y 9 (incluidos)")
    guess = int(input("Prueba otra vez: "))

while guess < numero:
    print("Es un número más alto")
    guess = int(input("Prueba otra vez: "))

while guess > numero:
    print("Es un número más bajo")
    guess = int(input("Prueba otra vez: "))
    
if guess == numero:
    print("¡Has acertado!")

