nome = input('Qual é o seu nome? ')

mai = nome.upper()

if mai == 'LEONARDO':
    print("Que nome maravilhoso!!")
else:
    print('Que nome comum!!') 

print(f'Bom dia, {mai}! ')

##############################################################################

n1 = float(input('Qual foi sua primeira nota = '))
n2 = float(input('Qual foi sua segunda nota = '))

m = (n1 + n2)/2

print(m)
if m >= 7.0:
    print('Parabéss você passou')
else:
    print('Recuperação')

