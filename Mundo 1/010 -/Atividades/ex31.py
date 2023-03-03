viagem = int(input('Qual a distância viajada? '))

a = viagem * 0.5
b = viagem * 0.45

if viagem <= 200:
    print(f'O valor de sua viagem será de {a}')
else: 
    print(f'Já nesse caso será {b}')
