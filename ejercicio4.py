for numero in range(1, 10):
    if numero < 5:
        print("* " * numero)
    else:
        print("* " * (10 - numero))

n=5
for i in range(1, n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
	