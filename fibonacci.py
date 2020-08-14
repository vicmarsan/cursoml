
# fibonacci_sequence = [0, 1]
# resultado = 7
# while resultado < 50:
#     resultado = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#     fibonacci_sequence.append(resultado)

# print (fibonacci_sequence)


fibonacci_sequence = [0]
resultado = 1
while resultado < 50:
    fibonacci_sequence.append(resultado)
    resultado = fibonacci_sequence[-1] + fibonacci_sequence[-2]

print (fibonacci_sequence)