s = float(input('Qual o seu salario? '))

maior = (s * 0.1) + s
menor = (s * 0.15) + s

if s > 1250.00: 
    print(f'O seu salário é acima da méida, terá um aumento de 15%, ficando {maior}')
else:
    print(f'O seu salário é menor que a méida, terá um aumento de 10%, ficando {menor} ')