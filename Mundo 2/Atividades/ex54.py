# Não sei usar isso, mas é uma função possível do Python
#from datetime import date
#"variável" (2022) = date.today().year
menores = 0
maiores = 0
for c in range (0,7):
    nasc = int(input('Data de nascimento dessa pessoa = '))
    idade = 2022 - nasc

    if idade < 18:
        menores += 1
    else:
        maiores += 1
print(f'Ainda não atingiram a mairidade {menores} pessoas')    
print(f'Já atingiram a mairidade {maiores} pessoas')
