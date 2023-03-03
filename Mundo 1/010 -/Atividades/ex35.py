cd = int(input('Qual é o tamanho da reta? '))
co = int(input('Qual é o tamanho da reta? '))
h = int(input('Qual é o tamanho da reta? '))

if cd**2 + co**2 == h**2:
    print(f'Esses números formam um triângulo')
else:
    print(f'Não é possível')
