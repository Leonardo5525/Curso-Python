numero = int(input('Escolha um número = '))
print(numero)

# Porque aqui nesse caso não funciona "import random"
# Assim no final, "random.choice"?
from random import randint 
n = randint (0,5)
print(n)

if n == numero:
    print('Você acertou')
else:
    print('Perdeu')


