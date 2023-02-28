n = int(input('Escolha um número inteiro qualquer = '))

print('Que base de conversão deseja, 1 = binário, 2 = octal ou 3 = hexadecimal')

base = int(input('Escolha 1, 2 ou 3 = '))

if 1 == base:
    print(f'A base será binária {bin(n)}')
elif 2 == base:
    print(f'A base será octal {oct(n)}')
elif 3 == base:
    print(f'Abase será hexadecimal {hex(n)}')
else:
    print('Base será desconhecida')

