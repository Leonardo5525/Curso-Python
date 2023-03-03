menor = 0
maior = 0
for c in range (0,5):
    peso = float(input('Data de nascimento dessa pessoa = '))
    #significa que estou lendo o peso da primeira pessoa
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print (maior)
print(menor)