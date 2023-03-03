a = float(input('Escolha um número = '))
b = float(input('Escolha um número = '))
c = float(input('Escolha um número = '))

# Achar o menor
menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Achar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor número é  = {menor}')
print(f'O maior número é = {maior}')