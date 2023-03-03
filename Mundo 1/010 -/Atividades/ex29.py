velo = int(input('Qual a velocidade que passou no radar?  '))

multa = (velo - 80) * 7

if velo >= 80: 
    print(f'Você excedeu o limite de velocidade, sendo sua multa de {multa} reais')
else:
    print('Normal')

