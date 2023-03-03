frase = input('Escreva uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(junto, inverso)

if junto == inverso:
    print ('A frase é um palindromo')
else:
    print('Frase não é um palindromo')