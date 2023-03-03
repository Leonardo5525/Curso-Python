nasceu = int(input('Qual ano nasceu? '))
ano = int(input('Qual ano está? '))
idade = ano - nasceu
print(idade)

if idade == 18:
    print('Compareça ao tiro de guerra')
elif idade < 18:
    print(f'Ainda deverá comparecer ao tiro, falta {18 - idade} anos')
else:
    print(f'Já passou seu tempo, passou {idade - 18} anos')
