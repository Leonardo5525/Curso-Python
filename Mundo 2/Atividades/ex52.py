n = int(input('Número inteiro = '))
t = 0

for c in range (1, n + 1):
    if n%c == 0:
        print('\033[33m', end = ' ')
    else:
        print('\033[31m', end = ' ')
    t = t + 1
    print(c, end=' ')

if t >= 2:
    print(F'\nO número {n} é primo ')
