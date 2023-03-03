total = 0
media = 0
velho = 0
nvelho = ''
mulher20 = 0
for pessoa in range (1,5):
    nome = (input('Qual o nome? ')).strip()
    idade = float(input('Qual a idade? '))
    sexo = input('Qual o sexo [H/F]? ').strip()
    total = total + idade
    if pessoa == 1 and sexo in 'Hh':
        nvelho = nome
        velho = idade
    if sexo in 'Hh' and idade > velho:
        nvelho = nome
        velho = idade
    if sexo in 'Ff' and idade < 20:
        mulher20 = mulher20 + 1
media = total/3
print(f'A média de idade é {media:.2}')
print (f'O homem mais velho é {nvelho} e ele tem {velho} idade')
print(f'A lista tem {mulher20} com menos de 20 anos de idade')
