n1 = float(input('Qual foi sua nota 1 = '))
n2 = float(input('Qual foi sua nota 2 = '))

m = (n1 + n2)/ 2
if m < 5.0:
    print ('REPROVADO')
elif m > 5.0 and m <= 6.9:
    print('Recuperação')
else:
    print('Aprovadooooooooo')