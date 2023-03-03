
n = int(input('Escolha um número = '))
razao = int(input('Escolha a razao = '))

for c in range (n, razao*10, razao):
    print(c)

# PROFESSOR
primeiro = int(input('Primeiro termo = '))
razao = int(input('razao = '))
decimo = primeiro + (10-1) * razao

for c in range (primeiro, decimo + razao, razao):
    print (c)