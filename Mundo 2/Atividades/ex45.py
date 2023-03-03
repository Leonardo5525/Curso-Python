e = input('Escolha pedra, papel ou tesoura? ')
print(f'Você escolheu = {e}')
import random
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
print (f'PC escolheu = {pc}')

if pc == 'papel':
    if e == 'papel':
        print('Empate')
    elif e == 'pedra':
        print(' PC Ganhou ')
    elif e == 'tesoura':
        print ('Você ganhou')

if pc == 'pedra':
    if e == 'pedra':
        print('Empate')
    elif e == 'tesoura':
        print(' PC Ganhou ')
    elif e == 'papel':
        print ('Você ganhou')

if pc == 'tesoura':
    if e == 'tesoura':
        print('Empate')
    elif e == 'papel':
        print(' PC Ganhou ')
    elif e == 'pedra':
        print ('Você ganhou')
