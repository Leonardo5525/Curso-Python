a = int(input('Qual o tamanho da reta = '))
b = int(input('Qual o tamanho da reta = '))
c = int(input('Qual o tamanho da reta = '))

if a**2 + b**2 == c**2:
    print('É um triangulo')
else:
    print('Não é um triangulo')

if a == b and a == c and b == c:
    print('Triangulo equilátero')
elif a == b and a != c and b != c:
    print('Triangulo isóceles')
elif a != b and a!=c and c!=b:
    print ('Triangulo escaleno')
