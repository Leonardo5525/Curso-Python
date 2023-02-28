a = int(input('Quantos dias utilizou o carro?  '))
b = int(input('Quantos quilometros rodou?  '))

valugar = a * 60
vkilo = b * 0.15
total = vkilo + valugar

print(f'O valor total a pagar pelo aluguel do carro é de {total}')